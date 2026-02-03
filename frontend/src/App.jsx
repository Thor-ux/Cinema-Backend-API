import { BrowserRouter, Routes, Route } from "react-router-dom"
import Movies from "./pages/Movies"
import Booking from "./pages/Booking"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Movies />} />
        <Route path="/book/:id" element={<Booking />} />
      </Routes>
    </BrowserRouter>
  )
}
