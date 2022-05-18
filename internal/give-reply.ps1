param([string]$text = "")

try {
	# print reply on the console:
	" ← $text"

	# speak by text-to-speech (TTS):
	if (!$IsLinux) {
		$TTSVoice = New-Object -ComObject SAPI.SPVoice
		foreach ($Voice in $TTSVoice.GetVoices()) {
			if ($Voice.GetDescription() -like "*- English*") { $TTSVoice.Voice = $Voice }
		}
		[void]$TTSVoice.Speak($text)
	}
	exit 0 # success
} catch {
	"⚠️ Error in line $($_.InvocationInfo.ScriptLineNumber): $($Error[0])"
	exit 1
}
