# Todo 🎯

- [ ] First incorporate maj7, maj9, maj11, and maj13 chords

- [ ] Move `generate_notes_from_lib` into Class Chords
- [ ] How to analyze 'b5' in 'Bm7b5'

- Circle of fifth design
- Is graph related to this?
  - Imagine a key name is a class, and its instance includes all the chords it has, and scales sort?
  - Then we can define a rule how to reach a chord to another, like search in a graph adjacency list

Some tasks I can think of:

### Basics
- [ ] Generate notes
  - [ ] Generate the right notes given the chord name
  - [ ] Genrate the notes in a scale

- [ ] Generate chords
  - [ ] Give the notes, generate the possible name of the chord
  - [ ] Give the key, scales and mode, generate chord
  - [ ] Give the scales, generate the chords of this scale

### Advanced
- [ ] Generate a jazz common chord progression

### Nice-to-haves
- [ ] When generating intervals for minor scales,take whether harmonic, natural or melodic minor into consideration
- [ ] In analysing the chords name, using regex match, instead of using `startwith()`
- [ ] Add `B#` in the libray

### Features
- [x] Give a minor triad and generate its notes. E.g. `Bm7`