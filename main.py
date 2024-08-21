from typing import List

def generate_notes_from_lib(root: str, intervals: List[int], accidentals='sharps'):
    notes_sharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    notes_flats = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C']
    notes_lib = notes_sharps if accidentals == 'sharps' else notes_flats

    base = notes_lib.index(root) - notes_lib.index('C')
    notes = []
    count = base

    # Natural minor scales are derived from their relative major scales, which use flats.
    for interval in intervals:
        count += interval
        if count >= 12:
            count -= 12
        print(count)
        notes.append(notes_lib[count])
    return notes

class Chord:
    def __init__(self, name):
        self.name = name
        self.root = name[0]
        self.scale = name[1]
        self.seventh = name[2]
        # self.notes = get_notes(self.root, self.scale, self.seventh)

    def get_name(self):
        print(self.name)

    def get_notes_from_chords(self, root: str, scale: str, seventh: str):
        return self.get_notes_from_scales(root, scale)
    
    def get_notes_from_scales(self, root: str, scale: str):
        # for example, it's root == B, scale == 'm'
        if scale.startswith(('maj', 'M', '▵')):
            intervals = [0, 2, 2, 1, 2, 2, 2, 1]
            accidentals = 'sharps'
        elif scale == 'm':
            # We only consider natual minor here
            intervals = [0, 2, 1, 2, 2, 1, 2, 2]
            accidentals = 'flats'
        # Todo: diminished, half-whole scales
        return generate_notes_from_lib(root, intervals, accidentals)

# We want to generate the notes of Bm7b5
chord = Chord('Bm7b5')
print(chord.get_notes_from_chords('B', 'm', '7'))