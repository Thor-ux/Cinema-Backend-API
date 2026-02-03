const API_URL = "http://localhost:8000/api"

export async function getMovies() {
  const res = await fetch(`${API_URL}/movies/`)
  return res.json()
}

export async function bookTicket(showtime, seat) {
  const res = await fetch(`${API_URL}/book/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ showtime, seat })
  })
  return res.json()
}
