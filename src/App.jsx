import { Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import EvaluatorPage from './pages/EvaluatorPage'
import LoginPage from './pages/LoginPage'
import RegisterPage from './pages/RegisterPage'

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<EvaluatorPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="*" element={<h1>404 - Page Not Found</h1>} />
      </Routes>
    </>
  )
}

export default App