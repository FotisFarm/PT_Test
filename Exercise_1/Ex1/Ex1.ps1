#Get path of working directory
$sample = (Get-item $PSCommandPath).DirectoryName
Set-Location $sample

#Create txt file for writing the fullpaths
New-Item -Path $sample -Name "Ex1.txt"

#Recursively search in the given directories for directories named 'Action#'
$a = Get-ChildItem -Path (Join-path $sample 'Action[0-9]') -Recurse -Directory
 
#In each directory search for files named 'Script.mts'
foreach ($b in $a) {
    $c = Get-ChildItem -filter "Script.mts" -path $b
    if ($null -eq $c) { 
        Add-Content "Ex1.txt" -Value ($b)
    }
}


