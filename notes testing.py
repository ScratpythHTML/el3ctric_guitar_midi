from midi_notes import majors
from midi_notes import minors
from midi_notes import bluemajors
from midi_notes import blueminors

SCALES = [majors, minors, bluemajors, blueminors]

scale_type = 0
scale_key = 0

current = SCALES[scale_type][scale_key]
print(current.name)
print(current.notes)
print(current.notes[0], current.notes[3])
