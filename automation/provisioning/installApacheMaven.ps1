# Common expression logging and error handling function, copied, not referenced to ensure atomic process
function executeExpression ($expression) {
	$error.clear()
	Write-Host "$expression"
	try {
		Invoke-Expression $expression
	    if(!$?) { Write-Host "[$scriptName] `$? = $?"; exit 1 }
	} catch { echo $_.Exception|format-list -force; exit 2 }
    if ( $error[0] ) { Write-Host "[$scriptName] `$error[0] = $error"; exit 3 }
    if (( $LASTEXITCODE ) -and ( $LASTEXITCODE -ne 0 )) { Write-Host "[$scriptName] `$LASTEXITCODE = $LASTEXITCODE "; exit $LASTEXITCODE }
}

# Cater for media directory being inaccesible, i.e. Vagrant/Hyper-V
function listAndContinue {
	Write-Host "[$scriptName] Error accessing cache falling back to `$env:temp"
	$mediaDir = $env:temp
	$fullpath = $mediaDir + '\' + $file
	return $fullpath
}

cmd /c "exit 0"
Add-Type -AssemblyName System.IO.Compression.FileSystem

$scriptName = 'installApacheMaven.ps1'

Write-Host "`n[$scriptName] ---------- start ----------"

$maven_version = $args[0]
if ( $maven_version ) {
	Write-Host "[$scriptName] maven_version         : $maven_version"
} else {
	$maven_version = '3.5.3'
	Write-Host "[$scriptName] maven_version         : $maven_version (default)"
}

$mediaDirectory = $args[1]
if ( $mediaDirectory ) {
	Write-Host "[$scriptName] mediaDirectory        : $mediaDirectory"
} else {
	$mediaDirectory = 'C:\.provision'
	Write-Host "[$scriptName] mediaDirectory        : $mediaDirectory (default)"
}

$destinationInstallDir = $args[2]
if ( $destinationInstallDir ) {
	Write-Host "[$scriptName] destinationInstallDir : $destinationInstallDir"
} else {
	$destinationInstallDir = 'c:\apache'
	Write-Host "[$scriptName] destinationInstallDir : $destinationInstallDir (default)"
}

if ( Test-Path $mediaDirectory ) {
	Write-Host "`n[$scriptName] $mediaDirectory exists"
} else {
	Write-Host "`n[$scriptName] $(mkdir $mediaDirectory) created"
}

# The installation directory for JDK, the script will create this
$target = 'apache-maven-' + $maven_version
$mediaFileName = $target + "-bin.zip"
Write-Host
if ( Test-Path $mediaDirectory\$mediaFileName ) {
	Write-Host "`n[$scriptName] Source media found ($mediaDirectory\$mediaFileName)"
} else { 
	Write-Host "`n[$scriptName] $file does not exist in $mediaDir, listing contents"
	try {
		Get-ChildItem $mediaDir | Format-Table name
	    if(!$?) { $installFile = listAndContinue }
	} catch { $installFile = listAndContinue }

	Write-Host "[$scriptName] Attempt download"
	$uri = "https://archive.apache.org/dist/maven/maven-3/${maven_version}/binaries/" + $mediaFileName
	executeExpression "(New-Object System.Net.WebClient).DownloadFile('$uri', '$mediaDirectory\$mediaFileName')"
}

Write-Host "[$scriptName] Maven media is packaged as a directory (apache-maven-$maven_version)"
if ( Test-Path $destinationInstallDir\$target ) {
	Write-Host "`n[$scriptName] Target ($destinationInstallDir\$target) exists, remove first"
	executeExpression "Remove-Item -Recurse -Force $destinationInstallDir\$target"
}

if ( Test-Path $destinationInstallDir ) {
	Write-Host "`n[$scriptName] destinationInstallDir ($destinationInstallDir) exists"
} else { 
	Write-Host "`n[$scriptName] Create destinationInstallDir ($destinationInstallDir)"
	executeExpression "New-Item -path $destinationInstallDir -type directory"
}

executeExpression "[System.IO.Compression.ZipFile]::ExtractToDirectory('$mediaDirectory\$mediaFileName', '$destinationInstallDir')"

Write-Host "`n[$scriptName] Add Maven to PATH"
$pathEnvVar=[System.Environment]::GetEnvironmentVariable("PATH","Machine")
executeExpression "[System.Environment]::SetEnvironmentVariable('PATH', `"$pathEnvVar`" + `";$destinationInstallDir\apache-maven-$maven_version\bin`", 'Machine')"

# Reload the path (without logging off and back on)
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Reload the path (without logging off and back on)
$versionTest = cmd /c mvn --version 2`>`&1
if ($versionTest -like '*not recognized*') {
	Write-Host "`n[$scriptName] Maven not installed! Exit with LASTEXITCODE 8546"
	exit 8546
} else {
	$array = $versionTest.split(" ")
	Write-Host "`n[$scriptName] Maven : $($array[2])"
}

Write-Host "`n[$scriptName] ---------- stop -----------`n"
exit 0