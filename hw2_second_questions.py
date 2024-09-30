# %%
#Question 4
def has_experience_as(cvs, job_title):
    # Initialize an empty list to store the usernames
    users_with_experience = []

    # Iterate through each CV in the list
    for cv in cvs:
        # Check if the job title is in the user's jobs
        if job_title in cv['jobs']:
            # Add the username to the list
            users_with_experience.append(cv['user'])

    return users_with_experience

# Example usage
cvs = [
    {'user': 'maria', 'jobs': ['analyst', 'doctor']},
    {'user': 'isabel', 'jobs': ['finance', 'biologist']},
    {'user': 'george', 'jobs': ['vet', 'judge', 'singer']},
    {'user': 'alice', 'jobs': ['engineer', 'designer']}
]

# Check for users with experience as 'engineer'
result = has_experience_as(cvs, 'doctor')
print(result)  # Output: ['john', 'alice']

# %%
#Question 5
def job_counts(cvs):
    # Initialize an empty dictionary to store job counts
    job_count_dict = {}

    # Iterate through each CV in the list
    for cv in cvs:
        # Iterate through each job in the user's jobs
        for job in cv['jobs']:
            # Increment the job count in the dictionary
            if job in job_count_dict:
                job_count_dict[job] += 1
            else:
                job_count_dict[job] = 1

    return job_count_dict

# Example usage
cvs = [
    {'user': 'maria', 'jobs': ['analyst', 'doctor']},
    {'user': 'isabel', 'jobs': ['finance', 'biologist']},
    {'user': 'george', 'jobs': ['vet', 'judge', 'singer']},
    {'user': 'alice', 'jobs': ['engineer', 'designer']}
]

# Get job counts that has one parameter list cvs and returns a dictionary where the keys are the job titles and the values are the number of users that have done that job
result = job_counts(cvs)
print(result)  

# %%
#Question 6
def most_popular_job(cvs):
    # Get the job counts using the job_counts function
    job_count_dict = job_counts(cvs)

    # Find the job with the maximum count
    most_popular = max(job_count_dict.items(), key=lambda x: x[1])
    
    return most_popular  # This will return a tuple (job_title, count)

# Example usage
cvs = [
    {'user': 'maria', 'jobs': ['analyst', 'doctor']},
    {'user': 'isabel', 'jobs': ['finance', 'biologist']},
    {'user': 'george', 'jobs': ['vet', 'judge', 'singer']},
    {'user': 'alice', 'jobs': ['engineer', 'designer']},
    {'user': 'bob', 'jobs': ['engineer', 'doctor']},
    {'user': 'bob', 'jobs': ['engineer', 'biologist']}
]

# Get the most popular job
result = most_popular_job(cvs)
print(result)  # Output might be: ('engineer', 2)


