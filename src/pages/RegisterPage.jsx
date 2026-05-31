import { useState } from 'react'
import { Link } from 'react-router-dom'

function RegisterPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')

  function handleSubmit(e) {
    e.preventDefault()
    console.log('Email:', email)
    console.log('Password:', password)
    console.log('Confirm Password:', confirmPassword)
  }

  return (
    <main>
      <section className="panel" style={{ maxWidth: '480px', margin: '2rem auto' }}>
        <h2>Register</h2>
        <form onSubmit={handleSubmit}>

          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            placeholder="name@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <label htmlFor="confirm-password">Confirm Password</label>
          <input
            type="password"
            id="confirm-password"
            placeholder="Confirm your password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />

          <button type="submit" className="register-btn">Register</button>

        </form>
        <p style={{ marginTop: '1rem', textAlign: 'center' }}>
          Already have an account? <Link to="/login">Login</Link>
        </p>
      </section>
    </main>
  )
}

export default RegisterPage