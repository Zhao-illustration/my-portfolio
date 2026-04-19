const ARTWORK_VARIANTS = {
  thumbMobile: "images/thumb-mobile",
  thumbDesktop: "images/thumb-desktop",
  largeMobile: "images/large-mobile",
  largeDesktop: "images/large-desktop"
};

const ARTWORKS = [
  {
    title: "Chaotic Dream",
    year: "2025",
    date: "2025",
    fileName: "1.jpg",
    alt: "Chaotic Dream",
    width: 2048,
    height: 2048,
    description: "Born from my experience of Salmon Run, this piece reflects on the fragility of life and the relentless urge to survive in the face of inevitable death."
  },
  {
    title: "Emergency Rescue",
    year: "2025",
    date: "2025",
    fileName: "2.jpg",
    alt: "Emergency Rescue",
    width: 2048,
    height: 2048,
    description: ""
  },
  {
    title: "Decompostion",
    year: "2025",
    date: "2025",
    fileName: "3.jpg",
    alt: "Decompostion",
    width: 2048,
    height: 2048,
    description: "Set in a long-abandoned pool, this piece explores the subconscious through monsters dissecting fears I had not yet recognized"
  },
  {
    title: "West absurdity",
    year: "2023",
    date: "2023",
    fileName: "4.jpg",
    alt: "West absurdity",
    width: 2048,
    height: 2048,
    description: "This piece explores my confusion and shifting beliefs as I moved from the Eastern to the Western country, questioning previously unwavering views on religion, culture and customs and reflecting the uncertainty of my own identity and the third space experience."
  },
  {
    title: "Rumor",
    year: "2022",
    date: "2022",
    fileName: "5.jpg",
    alt: "Rumor",
    width: 2048,
    height: 2048,
    description: "A twisted word\n grows many hands.\n Faceless,\n it lives from mouth to mouth.\n Before truth steps in,\n echoes fill the house."
  },
  {
    title: "Begging",
    year: "2025",
    date: "2025",
    fileName: "6.jpg",
    alt: "Begging",
    width: 2048,
    height: 2048,
    description: "This piece depicts the stark contrast between a homeless man in the subway and a tycoon hiding a corpse, reflecting social disparity and hidden darkness."
  },
  {
    title: "Sushi Monster",
    year: "2022",
    date: "2022",
    fileName: "7.jpg",
    alt: "Sushi Monster",
    width: 2046,
    height: 2047,
    description: "This work reflects the high demands placed on kitchen labor in the restaurant industry, and the way capital shapes food pricing, presentation, and the values behind dining culture."
  },
  {
    title: "Caged Bird",
    year: "2023",
    date: "2023",
    fileName: "8.jpg",
    alt: "Caged Bird",
    width: 2048,
    height: 2048,
    description: "After keeping parrots for several years, I began to question whether animals should live in cages. This work reflects my thoughts on animal rights, captivity, and the responsibility of the owner."
  },
  {
    title: "Dream in the Fish Tank",
    year: "2023",
    date: "2023",
    fileName: "9.jpg",
    alt: "Dream in the Fish Tank",
    width: 2048,
    height: 2048,
    description: "A dream within a dream, exploring the judgment, tension, and self-examination of my inner desires."
  },
  {
    title: "Pink Dream",
    year: "2025",
    date: "2025",
    fileName: "Untitled_Artwork 9.jpg",
    alt: "Pink Dream",
    width: 2048,
    height: 2048,
    description: "A dream-like work that explores lust, inner desire, fear, satisfaction, and the complex tension between these emotions."
  },
  {
    title: "SuperEgo",
    year: "2025",
    date: "2025",
    fileName: "Untitled_Artwork 10.jpg",
    alt: "SuperEgo",
    width: 2824,
    height: 2048,
    description: "This work explores the role of the soul and spirit beyond the physical body, both within the inner self and in the outer world. Inspired by Conversations with God by Neale Donald Walsch, it reflects a sense of awe, worship, and fear toward higher dimensions of existence."
  }
];

function swapExtension(fileName, extension) {
  return fileName.replace(/\.[^.]+$/, `.${extension}`);
}

function getArtworkAssetPath(work, variant, extension = "jpg") {
  return encodeURI(`${ARTWORK_VARIANTS[variant]}/${swapExtension(work.fileName, extension)}`);
}
