import requests
import json
from plate import repo
from plate import access_token
from plate import owner
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import statistics
import pandas as pd
import plotly.graph_objs as go

def get_contributors():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/stats/contributors"
        headers = {"Authorization": f"Bearer {access_token}"}


        response = requests.get(url, headers=headers)
        contributors = response.json()
        #print(contributors)
        #for contributor in contributors:
            #print("Contributor:")
            #print(f"\tID: {contributor['author']['id']}")
            #print(f"\tLogin: {contributor['author']['login']}")
            #print(f"\tTotal commits: {contributor['total']}")
            #print("Weeks:")
        #for week in contributor['weeks']:
            #print(f"\tStart of week: {week['w']}")
            #print(f"\tNumber of additions: {week['a']}")
            #print(f"\tNumber of deletions: {week['d']}")
            #print(f"\tNumber of commits: {week['c']}")
            #print(f"\tEnd of week: {week['w'] + 604800}") # 604800 seconds = 1 week

        frame_div = []
        for contributor in contributors:
            #print(f"\tTotal commits: {contributor['total']}")
            frame_div.append(contributor['total'])

        #print(frame_div)
        commits_average = sum(frame_div) / len(frame_div)
        #print(commits_average)

        list_high_average = []
        for contributor in contributors:
            if contributor['total'] > commits_average:
                list_high_average.append(contributor['author']['login'])

        all_commits = sum(frame_div)
        print('Number of regular contributors to TON Footsteps -', len(list_high_average))
        num_active_contributors = sum(1 for c in contributors if c["total"] > 0)
        print('Number of active contributors to TON Footsteps initiatives -',num_active_contributors)
        print('Number of contributions made by community members -', all_commits)
    except:
        print('Something Wrong...Try later')

def get_issues():
    url = f"https://api.github.com/repos/ton-society/{repo}/issues"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"per_page": 30, "state": "all"}

    getting_issues = []
    page_number = 1
    while True:
        params["page"] = page_number
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            break

        page_issues = response.json()
        if not page_issues:
            break

        getting_issues.extend(page_issues)
        page_number += 1

    issues_container = []
    for issue in getting_issues:
        issues_container.append(issue['number'])

    open_issues = []
    closed_issues = []

    for issue in getting_issues:
        if issue["state"] == "open":
            open_issues.append(issue)
        elif issue["state"] == "closed":
            closed_issues.append(issue)

    return {
        'Number issues': len(issues_container),
        'Number closed issues': len(closed_issues),
        'Number open issues': len(open_issues)
    }


def get_pulls():
    url = f"https://api.github.com/repos/ton-society/{repo}/pulls"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"per_page": 30, "state": "all"}

    getting_pulls = []
    page_number = 1
    while True:
        params["page"] = page_number
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            break

        page_pulls = response.json()
        if not page_pulls:
            break

        getting_pulls.extend(page_pulls)
        page_number += 1

    open_pulls = []
    closed_pulls = []

    for pull in getting_pulls:
        if pull["state"] == "open":
            open_pulls.append(pull)
        elif pull["state"] == "closed":
            closed_pulls.append(pull)

    return {
        'Number of pulls': len(closed_pulls) + len(open_pulls)
    }


def average_time_isseu():
    url = "https://api.github.com/repos/ton-society/ton-footsteps/issues"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"state": "all", "per_page": 100}

    all_issues = []
    delta_times = []

    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
        issues = response.json()
        if not issues:
            break
        for issue in issues:
            if issue.get("closed_at"):
                created_time = datetime.strptime(issue["created_at"], '%Y-%m-%dT%H:%M:%SZ').timestamp()
                closed_time = datetime.strptime(issue["closed_at"], '%Y-%m-%dT%H:%M:%SZ').timestamp()
                delta_times.append(closed_time - created_time)
                all_issues.append(issue)
        params["page"] = params.get("page", 1) + 1


    average_time = statistics.mean(delta_times) // 86400
    print(f"Average solving time: {average_time} days")

def get_data_contributors():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/stats/contributors"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url, headers=headers)
        contributors = response.json()

        frame_div = []
        for contributor in contributors:
            frame_div.append(contributor['total'])

        commits_average = sum(frame_div) / len(frame_div)

        list_high_average = []
        for contributor in contributors:
            if contributor['total'] > commits_average:
                list_high_average.append(contributor['author']['login'])

        all_commits = sum(frame_div)


        data = {
            'regular contributors': len(list_high_average),
            'active contributors': sum(1 for c in contributors if c["total"] > 0),
            'total contributions': all_commits
        }

        df = pd.DataFrame(data, index=[0])
        df.to_csv('contributors.csv', index=False)

    except:
        print('Something Wrong...Try later')

def data_get_issues():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url, headers=headers)
        issues = response.json()

        df = pd.DataFrame(issues)
        df.to_csv("issues.csv", index=False)

    except:
        print('Something Wrong...Try later')

def data_get_pulls():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url, headers=headers)
        pulls = response.json()


        df = pd.DataFrame(pulls)
        df.to_csv("pulls.csv", index=False)

    except:
        print('Something Wrong...Try later')

def data_average_time_issue():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url, headers=headers)
        issues = response.json()

        df = pd.DataFrame(average_time_issue)
        df.to_csv("average_time_issue.csv", index=False)

    except:
        print('Something Wrong...Try later')

def charts_contributors():
    try:
        contributors_df = pd.read_csv('contributors.csv')
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.bar(['Active', 'Regular'], [contributors_df['active contributors'][0], contributors_df['regular contributors'][0]])
        ax.set_xlabel('Contributor Type')
        ax.set_ylabel('Number of Contributors')
        ax.set_title('Active vs Regular Contributors')
        plt.show()
    except:
        print('Something Wrong...Try later')

def plot_contributors():
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/stats/contributors"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url, headers=headers)
        contributors = response.json()
        commits = [contributor['total'] for contributor in contributors]

        fig = go.Figure(
            data=[go.Bar(x=[contributor['author']['login'] for contributor in contributors], y=commits)],
            layout_title_text="Total Commits by Contributor"
        )

        fig.show()
    except:
        print("Something wrong...Try later")

def plot_issues():
    try:
        url = f"https://api.github.com/repos/ton-society/{repo}/issues"
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"per_page": 30, "state": "all"}

        getting_issues = []
        page_number = 1
        while True:
            params["page"] = page_number
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                break

            page_issues = response.json()
            if not page_issues:
                break

            getting_issues.extend(page_issues)
            page_number += 1


        open_issues = []
        closed_issues = []

        for issue in getting_issues:
            if issue["state"] == "open":
                open_issues.append(issue)
            elif issue["state"] == "closed":
                closed_issues.append(issue)

        fig = go.Figure(
            data=[go.Pie(labels=["Open Issues", "Closed Issues"], values=[len(open_issues), len(closed_issues)])],
            layout_title_text="Open vs. Closed Issues"
        )

        fig.show()
    except:
        print("Something wrong...Try later")


def plot_pulls():
    try:
        url = f"https://api.github.com/repos/ton-society/{repo}/pulls"
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"per_page": 30, "state": "all"}

        getting_pulls = []
        page_number = 1
        while True:
            params["page"] = page_number
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                break

            page_pulls = response.json()
            if not page_pulls:
                break

            getting_pulls.extend(page_pulls)
            page_number += 1

        open_pulls = []
        closed_pulls = []

        for pull in getting_pulls:
            if pull["state"] == "open":
                open_pulls.append(pull)
            elif pull["state"] == "closed":
                closed_pulls.append(pull)

        fig = go.Figure(
            data=[go.Pie(labels=["Open Pull Requests", "Closed Pull Requests"], values=[len(open_pulls), len(closed_pulls)])],
            layout_title_text="Open vs. Closed Pull Requests"
        )

        fig.show()
    except:
        print("Something wrong...Try later")

def issues_x_pulls():
    try:
        issues_count = len(get_issues())
        pulls_count = len(get_pulls())
        fig = go.Figure(data=[go.Bar(x=['Issues'], y=[issues_count], name='Issues', marker_color='#8B008B'),
                              go.Bar(x=['Pull Requests'], y=[pulls_count], name='Pull Requests', marker_color='#A9A9A9')])

        fig.update_layout(title_text='Number of open tasks and merge requests')

        fig.update_xaxes(title_text="Type")
        fig.update_yaxes(title_text="Quantity")

        fig.show()
    except:
        print("Something wrong...Try later")
