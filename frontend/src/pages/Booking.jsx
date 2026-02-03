import { useEffect, useState } from "react"
import SeatGrid from "../components/SeatGrid"
import { bookTicket } from "../api/api"

export default function Booking() {
  const [seats, setSeats] = useState([])
  const [selectedSeat, setSelectedSeat] = useState(null)

  useEffect(() => {
    fetch("http://localhost:8000/api/seats/1/")
      .then(res => res.json())
      .then(setSeats)
  }, [])

  const handleBook = async () => {
    const res = await bookTicket(1, selectedSeat.id)
    alert("Booking code: " + res.booking_code)
  }

  return (
    <div>
      <h2>Select seat</h2>
      <SeatGrid
        seats={seats}
        selectedSeat={selectedSeat}
        onSelect={setSelectedSeat}
      />
      <button disabled={!selectedSeat} onClick={handleBook}>
        Book seat
      </button>
    </div>
  )
}
