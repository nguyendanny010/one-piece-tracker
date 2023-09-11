class Manga {
  readonly title: String;
  readonly arcs: Arc[];
  currentChapter: number;
  numberOfChapters: number;
  latestChapter!: number;

  constructor(
    title: String,
    arc: Arc[],
    currentChapter: number,
    numberOfChapters: number,
    latestChapter: number
  ) {
    this.title = title;
    this.arcs = arc;
    this.currentChapter = currentChapter;
    this.numberOfChapters = numberOfChapters;
    this.latestChapter = latestChapter;
  }

  get getCurrentChapter(){
    return this.currentChapter;
  }
  get getTitle(){
    return this.title;
  }
  get getArcs(){
    return this.arcs;
  }
  get getNumberOfChapters(){
    return this.numberOfChapters;
  }
  get getLatestChapter(){
    return this.latestChapter;
  }
  set setCurrentChapter(currentChapter: number){
    this.currentChapter = currentChapter;
  }
  set setNumberOfChapters(numberOfChapters: number){
    this.numberOfChapters = numberOfChapters;
  }
  set setLatestChapter(latestChapter: number){
    this.latestChapter = latestChapter;
  }
}
