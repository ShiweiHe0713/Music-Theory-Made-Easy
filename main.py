from typing import List

def generate_notes_from_lib(root: str, intervals: List[int], accidentals='sharps'):
    notes_sharps = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B', 12: 'C'}
    notes_flats = {0: 'C', 1: 'Db', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb', 7: 'G', 8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B', 12: 'C'}
    notes_lib = notes_sharps if accidentals == 'sharps' else notes_flats

    notes = []
    count = 0
    # Natural minor scales are derived from their relative major scales, which use flats.
    for interval in intervals:
        count += interval
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
print(chord.get_notes_from_chords('C', 'm', '7'))