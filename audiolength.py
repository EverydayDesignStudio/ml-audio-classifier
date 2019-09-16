def audiolength(audio):
    import os
    from pydub import AudioSegment
    sound = AudioSegment.from_file(audio)
    sound_time=sound.duration_seconds
    return sound_time