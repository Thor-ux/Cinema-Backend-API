import { useEffect, useState } from "react"
import { getMovies } from "../api/api"

export default function Movies() {
  const [movies, setMovies] = useState([])

  useEffect(() => {
    getMovies().then(setMovies)
  }, [])

  return (
    <div>
      <h1>Movies</h1>
      {movies.map(movie => (
        <div key={movie.id}>
          <h3>{movie.title}</h3>
          <p>{movie.description}</p>
        </div>
      ))}
    </div>
  )
}
