from fastmcp import FastMCP
import requests

mcp = FastMCP("HH MCP Server")

@mcp.tool()
def search_vacancies(query: str):
    url = "https://api.hh.ru/vacancies"

    params = {
        "text": query,
        "per_page": 20
    }

    response = requests.get(url, params=params)

    return response.json()

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )
