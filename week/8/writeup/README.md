Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Corbett Blair
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Corbett Blair

## Assignment 8 Writeup

### Part 1 (45 Pts)

1. Yes, traceroute was used.

2.laz0rh4x and c0uchpot4doz. They are connecting from San Francisco and Baltimore, respectively.

3.laz0rh4x IP: 104.248.224.85

  c0uchpot4d0z IP: 206.189.113.189  

4. Port 2749

5. They didn't mention their plans specifically but said there were outlined in the google drive file, which can be parsed using the parser laz0rh4x sent c0uchpot4doz. The plans are going to be executed tomorrow at 1500.

6. laz0rh4x sent this google drive file to c0uchpot4d0z:

https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing


7. The hackers said they will see each other tomorrow. The plan is happening at 1500 (3:00 pm) so that is likely when they will meet.

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

1. It was generated on 10/25/18 at 12:40 am.

2. It was authored by laz0rh4x

3. It says there are 9 sections. There are actually 10 sections.

4. Section 1: SECTION_ASCII: "Call this number to get your flag: (422) 537 - 7946'

  Section 2: SECTION_WORDS: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

  Section 3: SECTION_COORD:  LONGITUTE: 38 LATITUDE: -77

  Section 4: SECTION_REFERENCE: 1

  Section 5: SECTION_ASCII: ('The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}',)

  Section 6: SECTION_COORD: LONGITUDE: 38 LATITUDE: -76

  Section 7: SECTION_PNG: Could not get it to open

  Section 8: SECTION_ASCII: ('AF(saSAdf1AD)Snz**asd1',)

  Section 9: SECTION_ASCII: ('Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9\n',)

  Section 10: SECTION_DWORDS: [2e-323, 4e-323, 7.4e-323, 8e-323, 1.14e-322, 2.08e-322]



5. Flag from phone: US01LV
Flag from text: PlaIN_IfF_FLAG
