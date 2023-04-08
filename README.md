# Saturn MF - Integrated analytics 
## Intro 
The complex is presented in the form of two modules + plate file (for access data) and Markdown tutorial how to use it

## Saturn_M 
### Introduction:

# The Saturn MF project is a GitHub repository that **tracks contributions** to the TON blockchain. This project allows users to see how many people are actively contributing to the repository, how many issues are open, and how long it takes to resolve them. The project uses the GitHub API to gather data from the repository.

The Python module "Saturn_M" provides users with the following functions:
- ```get_contributors()```: This function returns the number of contributors to the TON Footsteps project and the number of active contributors to the project. It also displays the number of contributions made by the community members.
- ```get_issues()```: This function returns the number of issues in the TON Footsteps project, the number of open issues, and the number of closed issues.
- ```get_pulls()```: This function returns the number of pull requests in the TON Footsteps project.
- ```average_time_isseu()```: This function calculates the average time it takes to resolve an issue in the TON Footsteps project.

Let's look at each function in detail:
```get_contributors():```

The ```get_contributors()``` function returns the number of contributors to the ***TON Footsteps project and the number of active contributors to the project.*** It also displays ***the number of contributions made by the community members.

The function first calls ***the GitHub API*** to get the data for the TON Footsteps project. It then calculates the **average number of commits per contributor** and **identifies the contributors who have made more than the average number of commits.** The function then displays the number of regular contributors to the project, the number of active contributors to the project, and the total number of contributions made by the community members.

```get_issues()```

The ```get_issues()``` function returns the ***number of issues in the TON Footsteps project, the number of open issues, and the number of closed issues.***

The function first calls the GitHub API to get the data for the TON Footsteps project. It then separates the issues into two lists based on whether they are open or closed. The function then returns the total number of issues, the number of open issues, and the number of closed issues.

```get_pulls()```

The **get_pulls()** function returns the number of pull requests in the TON Footsteps project.

The function first calls the GitHub API to get the data for the TON Footsteps project. It then separates the pull requests into two lists based on whether they are open or closed. The function then returns the total number of pull requests.

    average_time_isseu():

The average_time_isseu() function calculates the average time it takes to resolve an issue in the TON Footsteps project.

The function first calls the GitHub API to get the data for the TON Footsteps project. It then calculates the time it takes to resolve each issue by subtracting the time the issue was created from the time it was closed. The function then calculates the average time it takes to resolve an issue and returns the result.

Conclusion:

The Python module provides users with several functions that allow them to gather data from the TON Footsteps project on GitHub. The data returned by the functions can be used to track the progress of the project and identify areas that need improvement. With the help of these functions, users can get a better understanding of the contributions made by the community members and identify the active contributors to the project.
