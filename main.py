from fastapi import FastAPI, __version__
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = f"""
<!DOCTYPE html>
<html>

<head>
  <title>Indian Startup Ecosystem Data Analysis</title>
</head>

<body>
  <h1>Indian Startup Ecosystem Data Analysis</h1>

  <p>This data analysis task aims to provide a comprehensive overview of the Indian startup ecosystem, focusing on the period from 2018 to 2021. By examining a rich dataset encompassing this timeframe, we aim to uncover key trends, patterns, and insights that shed light on the dynamic nature of India's startup landscape.</p>

  <h2>Summary</h2>

  <table>
    <tr>
      <th>Code</th>
      <th>Name</th>
      <th>Published Article</th>
      <th>Deployed App</th>
    </tr>
    <tr>
      <td>LP 1</td>
      <td>Indian Startup Ecosystem Data Analysis</td>
      <td><a href="https://www.linkedin.com/pulse/india-startup-ecosystem-data-analysts-view-solomon-nyamson">Published Article</a></td>
      <td><a href="https://app.powerbi.com/view?r=eyJrIjoiYjI3M2Y3ZDAtZmEwOC00MzJjLThiZDEtYTU2NzcyNTJkZTgxIiwidCI6IjQ0ODdiNTJmLWYxMTgtNDgzMC1iNDlkLTNjMjk4Y2I3MTA3NSJ9">Power BI Dashboard</a></td>
    </tr>
  </table>

  <h2>Project Description</h2>

  <p>In recent years, India has witnessed a remarkable surge in entrepreneurial activities, propelling the growth of its startup ecosystem. With a burgeoning population, a thriving digital landscape, and a supportive environment for innovation and entrepreneurship, India has become a hotbed for startups across various industries.</p>

  <p>This data analysis task aims to provide a comprehensive overview of the Indian startup ecosystem, focusing on the period from 2018 to 2021. By examining a rich dataset encompassing this timeframe, we aim to uncover key trends, patterns, and insights that shed light on the dynamic nature of India's startup landscape.</p>

  <h2>Data Dictionary</h2>

  <table>
    <tr>
      <th>Column</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>Company/Brand</td>
      <td>Name of the company/start-up</td>
    </tr>
    <tr>
      <td>Founded</td>
      <td>Year start-up was founded</td>
    </tr>
    <tr>
      <td>Sector</td>
      <td>Sector of service</td>
    </tr>
    <tr>
      <td>What it does</td>
      <td>Description about the company</td>
    </tr>
    <tr>
      <td>Founders</td>
      <td>Founders of the company</td>
    </tr>
    <tr>
      <td>Investor</td>
      <td>Investors</td>
    </tr>
    <tr>
      <td>Amount($)</td>
      <td>Raised fund</td>
    </tr>
    <tr>
      <td>Stage</td>
      <td>Round of funding reached</td>
    </tr>
  </table>

  <h2>Setup</h2>

  <ol>
    <li>Install all the necessary libraries like <code>pandas, numpy, matplotlib, plotly</code></li>
    <li>Install pyodbc - a package for creating connection strings to your remote database</li>
    <li>Install python-dotenv - a package for creating environment variables that will help you hide sensitive configuration information such as database credentials and API keys</li>
    <li>Import all the necessary libraries
      <ul>
        <li><code>pyodbc</code> (for creating a connection)</li>
        <li><code>python-dotenv</code> (loading environment variables)</li>
      </ul>
    </li>
    <li>Now create a file called <code>.env</code> in the root of your project folder (Note, the file name begins with a dot)</li>
    <li>In the <code>.env</code> file, put all your sensitive information like server name, database name, username, and password</li>
  </ol>

  <h2>App Execution</h2>

  <p>The project is available in two formats: a published report and a deployed Power BI Dashboard.</p>

  <p>To access the Report, use the following link: <a href="https://www.linkedin.com/pulse/india-startup-ecosystem-data-analysts-view-solomon-nyamson">Report URL</a></p>

  <p>For the Deployed Dashboard, use the following link: <a href="https://app.powerbi.com/view?r=eyJrIjoiYjI3M2Y3ZDAtZmEwOC00MzJjLThiZDEtYTU2NzcyNTJkZTgxIiwidCI6IjQ0ODdiNTJmLWYxMTgtNDgzMC1iNDlkLTNjMjk4Y2I3MTA3NSJ9">Power BI Dashboard</a></p>

  <h2>Author</h2>

  <p>Solomon Nyamson</p>
</body>

</html>


"""


@app.get('/')
async def root():
    return HTMLResponse(html_content)