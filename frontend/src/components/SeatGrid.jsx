import Seat from "./Seat"
import "../styles/seats.css"

export default function SeatGrid({ seats, selectedSeat, onSelect }) {
  return (
    <div className="seat-grid">
      {seats.map(seat => (
        <Seat
          key={seat.id}
          seat={seat}
          isSelected={selectedSeat?.id === seat.id}
          onSelect={onSelect}
        />
      ))}
    </div>
  )
}
