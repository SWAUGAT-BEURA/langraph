from crewai import Agent,Task,Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

@CrewBase
class MarketingCrewai:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'],
            tools=[ScrapeWebsiteTool(),SerperDevTool()],
            verbose=True
        )

    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'],
            verbose=True
        )

    @agent
    def content_reviewer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['content_reviewer_agent'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agents=[self.research_agent],
            tools=[ScrapeWebsiteTool(),SerperDevTool()],
            verbose=True
        )

    @task
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['writer_task'],
            agents=[self.writer_agent],
            output_file="output/content.md",
            verbose=True
        )

    @task
    def content_reviewer_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_reviewer_task'],
            agents=[self.content_reviewer_agent],
            output_file="output/content_reviewed.md",
            verbose=True
        )


    @crew
    def marketing_crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
        )
        
    