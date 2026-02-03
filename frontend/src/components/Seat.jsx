export default function Seat({ seat, isSelected, onSelect }) {
  const className = `
    seat
    ${seat.seat_type === "VIP" ? "vip" : "regular"}
    ${seat.is_booked ? "booked" : ""}
    ${isSelected ? "selected" : ""}
  `

  return (
    <div
      className={className}
      onClick={() => !seat.is_booked && onSelect(seat)}
    >
      {seat.row_number}-{seat.seat_number}
    </div>
  )
}
