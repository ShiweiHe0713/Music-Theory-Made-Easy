# Music Theory Application
**Table of Content**
- [Music Theory Application](#music-theory-application)
  - [Keys 🎼](#keys-)
  - [Scales ♯](#scales-)
    - [Minor scales](#minor-scales)
      - [Natural minor scales](#natural-minor-scales)
      - [Harmonic minor scales](#harmonic-minor-scales)
      - [Melodic minor scales](#melodic-minor-scales)
  - [Chords 🎶](#chords-)
      - [How to form a chord?](#how-to-form-a-chord)
      - [Chord notation](#chord-notation)
    - [How to identify a chord?](#how-to-identify-a-chord)
    - [How to name a chord?](#how-to-name-a-chord)
    - [Compute or retrieve a chord?](#compute-or-retrieve-a-chord)
  - [Modes](#modes)
  - [Todo 🎯](#todo-)
    - [Basics](#basics)
    - [Advanced](#advanced)
    - [Nice-to-haves](#nice-to-haves)

## Keys 🎼

## Scales ♯
Let's build a `Bm7♭5(♭9)`(B, D, F, A, C) from a scale. The Bm7♭5(♭9) chord can be related to both the B diminished scale and the Locrian mode of C major, but the context and usage will differ.

In key of C major, we have C, D, E, F, G, A, B. So based on the 7 modes, we have 7 chords: **Cmaj7, Dm7, Em7, Fmaj7, G7, Am7, Bm7b5**. Whenever we have the key(C), scales(major) and mode(Locrian), we will have a chord.

### Minor scales
#### Natural minor scales
For example, A natual minor scales: A, B, C, D, E, F, G, A

#### Harmonic minor scales
For example, A harmonic minor scales: A, B, C, D, E, F, **G#**, A

#### Melodic minor scales
For example, A melodic minor scales: 
- A, B, C, D, E, F#, G#(ascending)
- A, G, F, E, D, C, B (descending)

## Chords 🎶
#### How to form a chord?
1. Key + scales + mode (To generate chords)
   - C + major + Lorcian = Bm7b5

2. Scales itself(To generate notes)
   - Bm7b5 can from the B half-whole diminished scale. 
   - B, C, D, D#, F, F#, G#, A
   - B + D + F + A = Bm7b5

#### Chord notation
[Wikipedia Reference](https://en.wikipedia.org/wiki/Chord_notation)
Chords consist of: root note, third, fifth, seventh, and other motiffs. For example, Fmaj7 will be a chord that has a root of F, it's a major chord, and a 7th(dominant) chord. **Chords can be viewed as root note plus many intervals.**

### How to identify a chord?
**Triad root + Type + 7th + Extended notes + Altered notes**
Example of Categorization:
- Cmaj7: C (root) + Major (type) + Major 7th
- C7: C (root) + Major (type) + Minor 7th (dominant)
- Cm7♭5: C (root) + Diminished (type) + Minor 7th
- C9: C (root) + Major (type) + Minor 7th (dominant) + 9th (extended)
- C7♯9♭5: C (root) + Major (type) + Minor 7th (dominant) + ♯9, ♭5 (altered)

### How to name a chord?
We can't simply concatenate 7th, 9th, 11th, and 13th to get a chord name. For example, `Cmaj13` chord is not called `Cmaj7 9 11 13`.

### Compute or retrieve a chord?
Imagine we enter a chord name, we want the program to spit out all the notes this chord has(or the other way around). We can simply store every chord and their notes in a hashmap, thus only require O(1) time to get a chord notes. However in this case, we will have to manually input all the chords inside the hashmap. It's not efficient and not smart. So we should still let the user type in the critial, unique identifiers of a chord, and our algorithm calculates out the chord notes or other things we need. 

**Should we think of scales? Cuz every scale can be a corresponding identifier for a chord!**

## Modes 


## Todo 🎯
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