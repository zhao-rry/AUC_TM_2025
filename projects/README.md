# Group projects

The project is the main grading item of the course. It will allow you to choose a dataset and question of interest, and run an analysis all the way to communicating its results. A project should be an analysis of a question or topic of interest, using text data. You can use the techniques we have seen in class and/or others as well. 

**The AUC Code of Conduct applies to this assignment: please only submit your group's work and reference sources where applicable.**

*Each group must have a GitHub (or GitLab) repository and use it to provide regular updates (see below).*

## Timeline

* **February 7** Guidelines and default project ideas out. Group formation opens on Canvas (you can self-organize, groups are capped to 3). Proposals for custom projects are encouraged.
* **April 4** Groups are formed, time to decide on a project idea, if you have not already. Discussions (with me) on how to structure your project should start ASAP.
* **April 11** Project update 0: repository `README` up. You need to submit a link to your repo containing the populated `README` file. This file should contain a detailed project plan, including: research question, dataset, methods, milestones, proposed division of work. Please use the [repository README template](README_template.md).
* **May 2** Project update 1 (see below for guidelines).
* **May 15** Project update 2 (see below for guidelines).
* **May 28/31** In-class presentations: 10+10 minutes (presentation + questions), schedule to be published in advance.
* **June 2 (23:59 CEST)** Project due for all groups.

## Practicalities

* **Team size**: teams of 3 people are strongly encouraged. One or two groups can be sized 2 or 4 if necessary (ask me first, the expected workload goes down or up accordingly). Groups of 1 are not allowed.
* **Contribution**: in the final report plase add a statement of what each team member contributed to the project. Team members will typically get the same grade, but I may differentiate in clear cases of unequal contribution. You can contact me in confidence in the event of unequal contribution.
*Example: John: Plotting graphs during data analysis, crawling the data, preliminary data analysis; Mary: Problem formulation, writing up the report, coming up with the algorithm; Chris: Coding up the algorithm, running tests, tabulating final results.*
* **Using external resources**: you may use any existing code, libraries, etc. and consult any papers, books, online references, generative language models, etc. for your project. However, you must cite your sources in your writeup and clearly indicate which parts of the project are your contribution and which parts were implemented by other authors or entities. Under no circumstances may you look at the code of another project from this course, or incorporate their code into your project. In your writeup, you cannot copy literally the output from external sources, including generative language models, even when you have cited those sources. This means that you *must* rework and process such information from external sources into your own writeup.
* **Logistics**: you must create your project's GitHub (or GitLab) repository and work there (one of you uses their account and the others are invited as collaborators). This will help you start your project portfolio online.
* **Updates**: these are brief summaries of what you have accomplished during the previous week, as well as any question you would like to ask. Groups should use a GitHub *issue* for every separate update, and add links to code or data where applicable. I will reply there. *You must submit updates, please do not have me chase you*: this is not optional and will influence your grade.
* **Final submission**. You are expected to **submit a public URL to your repository**, containing the following: a short **report** (4-page maximum, excluding references and appendix), a **slide deck** for your presentation (I recommend 5-10 slides, not more), the **repository** or folder containing code, data and a `README` file with appropriate documentation to navigate the repository (all this with a link to your repository). **Please put the bulk of the code into a single notebook, with a clear structure and dependences.** *Note that the slide deck can be updated after the group presentation, but should be in the repo at submission time.*

## Presentation

For the grading of the presentations, I will pay attention to the following points:

### Content

* Presentation of the background to your project
* Presentation of your key findings
* Critical appraisal of your project and results
* Presentation of the connection of your project to the course's topics

### Delivery

* Clarity
* Pacing (and time limit)
* Use of visual aids (slides etc.)
* Ability to engage the audience
* Ability to respond to questions (discussion)

## Set-up

1. [Repository README template](README_template.md).
2. [Some datasets you can consider](https://docs.google.com/spreadsheets/d/1DxHczqrAxlip1mA51BYSpygUrrNpiB1CaV3eiUC0DBs/edit?usp=sharing).
3. List of list of datasets:
    * https://github.com/niderhoff/nlp-datasets
    * https://github.com/karthikncode/nlp-datasets
    * https://github.com/awesomedata/awesome-public-datasets#naturallanguage
    * https://www.cooldatasets.com/
    * https://www.kaggle.com/datasets
    * https://en.wikipedia.org/wiki/List_of_text_corpora
    * https://neerlandistiek.nl/2018/09/de-beste-digitale-taalbronnen/
4. [Default project ideas](default_project_ideas.md).
5. Example projects. Please keep in mind some of these are from courses at the master level: do get inspired, but do not get worried.
    * [Projects from the previous-year edition](https://github.com/bloemj/AUC_TMCI_2022)
    * [Projects from 2021 edition](https://github.com/Giovanni1085/AUC_TMCI_2021)
    * [Projects from 2019 edition](https://github.com/Giovanni1085/AUC_TMCI_2019)
    * https://dlab.epfl.ch/teaching/fall2018/cs401/reports
    * https://www.epfl.ch/labs/mlo/machine-learning-cs-433
    * http://web.stanford.edu/class/cs224n/project.html
6. [Report template](report/): A 4-page, double-column PDF report (4 pages excluding references), following a standard structure (where applicable): abstract, introduction, related work, (brief) data collection, dataset description with summary statistics, methods with math and description of main algorithms, results and findings, conclusions. This report will be evaluated according to how clearly and succinctly it is written, if the style is appropriate (e.g., figures with captions), if it contains all relevant contents, and how solid the results are.

## Project grading

For the grading of the final projects, I will pay attention to the following points:

### Code and repository
* Does it run and properly load all its dependencies? Did you use relative paths so that others can run the code?
* Is your code readable (well-commented, well-structured with functions or code blocks) and documented, similar to the assignments?
* Is your data well-structured and documented, if applicable?
* Did you reference external resources that were used where necessary?
* Is the readme informative?

### Report

* **Author contributions**: Did you indicate who contributed what, and was this an effective division of tasks?
* **Background**: Does the problem and goal of the project become clear? Is the background information correct and would your classmates understand it?
* **Quality of the specific research question**: Is the question or topic addressed in the project related to text mining and can it be addressed by methods we learned about in the course?
* **Method and data**: Does the described approach/approaches effectively address (part of) the research question or problem? Are concrete enough details provided about the dataset(s) and methods(s) (algorithms, libraries) that you used? Are the essential properties of your dataset and how you collected it clearly described? Is there enough information that someone could reproduce the results of your project independently? Do you describe an effective validation/evaluation of your method?
* **Results**: Are the results well analysed, evaluated and presented?
* **Conclusions**: Are the results accurately summarized? Did you critically reflect upon your results? Are open issues and future work well covered?
* **Original contribution**: Did you find the academic literature that is the most similar to what you are doing? What is the novelty of your proposal compared to what is described in the literature (gap in the literature), and does the report make this clear without overselling your idea?

* **Clarity of expression**: Is the language in the report precise and accurate? Are you writing in an academic style/register while still remaining clear and not overusing jargon or uncommon/specific words?
* **Figures/graphs/tables**: If relevant, are they properly used?
* **Supplementary materials**: Does your report reference elements from your repository when appropriate?
* **Structure**: Are all the aspects of the standard structure (if applicable) correctly included and is the report well-structured?


