import { useState } from 'react'
import reactLogo from './assets/react.svg'
import Login from './containers/login';
import './index.css'
import { Routes, Route} from "react-router-dom";
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <Routes>
        <Route path="login" element={<Login />} />
        {/* <Route path="/*" element={<Home />} /> */}
      </Routes>

    </div>
  )
}

export default App
