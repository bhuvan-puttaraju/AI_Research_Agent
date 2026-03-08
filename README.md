# AI Research Agent

AI Research Agent is a simple project that demonstrates how multiple AI agents can work together to research a topic and generate a structured report. The idea behind this project is to automate the research process by allowing AI agents to plan the research, gather important information, and compile everything into a clear report.

The system is built using Python and uses a multi-agent workflow where each agent has a specific responsibility. Instead of one model doing everything, different agents collaborate to produce better results.

## Project Overview

This project simulates a small research team made up of AI agents. Each agent focuses on a particular task and passes the results to the next agent in the workflow.

The process begins when a user enters a topic to research. The system then creates a research plan, gathers useful insights from the web, and finally generates a complete research report.

## Agents in the System

**Triage Agent**

The triage agent acts as the coordinator of the system. It understands the user’s research topic and creates a plan that includes search queries and key areas to explore.

**Research Agent**

The research agent searches for relevant information related to the topic. It collects important insights and facts that will later be used to build the report.

**Editor Agent**

The editor agent takes all the collected information and turns it into a well-structured research report. It organizes the ideas into sections and produces a clear and readable document.

## Key Features

- Multi-agent research workflow
- Automatic research planning
- Web information gathering
- AI generated research reports
- Interactive Streamlit interface
- Fact collection during research
- Structured report generation

## Technologies Used

- Python
- Streamlit
- OpenAI Agents SDK
- Groq API
- Pydantic
- Python Dotenv
- AsyncIO

## Purpose of the Project

The main goal of this project is to explore how AI agents can collaborate to perform complex tasks like research and report generation. It demonstrates how multi-agent systems can break down a large problem into smaller tasks and solve them efficiently.

This project also showcases how AI can be used to automate information gathering and transform raw data into meaningful insights.
