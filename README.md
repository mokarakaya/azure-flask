# azure-flask

- Deploys a Flask Web application to Azure by using Github Actions
- App url: https://mokarakaya-hello-flask.azurewebsites.net/hello

## Steps

- `Create a Resource Group`: A resource group keeps resources e.g. web apps, databases, storage accounts etc.
- `Create a Web App`: We need to set the resource group while creating the web app.
- `Create an App Service Plan`: The plan is used to set server location, and pricing tier.
- `Create Deployment`: We use Deployment Center to configure deployment. Choose Github as source control, then select the project. Finally use Github Actions. Configuration files will be created in `.github`. The deployment will start automatically when selected branch (`main`) is changed.  