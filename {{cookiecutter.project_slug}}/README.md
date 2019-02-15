# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Development
The project configuration files are at the root level
The project sources are under the package {{cookiecutter.project_slug}}

Remember to declare {{cookiecutter.project_name}} as the Source Root for your code

## Deployment
Ensure the billing account is set and that Cloud Build is enabled 

    gcloud init
    gcloud auth login
    gcloud source repos create {{cookiecutter.project_slug}}
    
    git config --global credential.https://source.developers.google.com.helper gcloud.cmd
    git remote add google https://source.developers.google.com/p/{{cookiecutter.google_project_id}}/r/{{cookiecutter.project_slug}}
    git push --all google   # You may have to visit https://source.developers.google.com/new-password
    
To deploy your project on GCP, execute the following commands
    
    gcloud app deploy
    
To check your app running
    
    gcloud app browse
    
You may want to modify deployments options by editing the file [app.yaml]

''' See how to create gcloud command for trigger    
Cloud Build > Create Trigger from Google Repository