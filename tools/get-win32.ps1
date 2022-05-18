Get-CimInstance -ClassName Win32_BIOS
Get-CimInstance -ClassName Win32_ComputerSystem
Get-CimInstance -ClassName Win32_QuickFixEngineering

Write-Host "OS details"
Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object -Property Build*,OSType,ServicePack*

Write-Host "users and the owners"
Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object -Property *user*

Write-Host "disk space"
Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3" |Measure-Object -Property FreeSpace,Size -Sum |Select-Object -Property Property,Sum

Write-Host "Current user logged in to the system"
Get-CimInstance -ClassName Win32_ComputerSystem -Property UserName


