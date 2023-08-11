$sample = (Get-item $PSCommandPath).DirectoryName

Set-Location $sample
New-Item -Path $sample -Name "Ex1.txt"


$a = Get-ChildItem -Path (Join-path $sample 'Action[0-9]') -Recurse -Directory
 

foreach ($b in $a) {
    $c = Get-ChildItem -filter "Script.mts" -path $b
    if ($null -eq $c) { 
        Add-Content "Ex1.txt" -Value ($b)
    }
}


