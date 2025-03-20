#!/usr/bin/env python
from random import randint
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from research_flow.crews.poem_crew.poem_crew import PoemCrew

class PoemState(BaseModel):
    topic: str = ""
    research: str = ""

class PoemFlow(Flow[PoemState]):
    @start()
    def generate_topic(self):
        self.state.topic = 'Impact of AI in Education Sector'

    @listen(generate_topic)
    def generate_research(self):
        print("Generating research")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={"topic": self.state.topic})
        )
        print("Research generated", result.raw)
        self.state.research = result.raw

    @listen(generate_research)
    def save_research(self):
        print("Saving....")
        return {"research" : self.state.research, "topic": self.state.topic}

def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
