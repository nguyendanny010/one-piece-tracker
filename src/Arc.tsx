class Arc{
    readonly title: String;
    readonly startChapter: number;
    readonly endChapter: number;
    currentChapter: number;

    constructor(title: String, startChapter: number, endChapter: number){
        this.title = title;
        this.startChapter = startChapter;
        this.endChapter = endChapter;
        this.currentChapter = startChapter;
    }
}