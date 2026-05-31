import { useState } from 'react'
import { Link } from 'react-router-dom'

function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  function handleSubmit(e) {
    e.preventDefault()
    console.log('Email:', email)
    console.log('Password:', password)
  }

  return (
    <main>
      <section className="panel" style={{ maxWidth: '480px', margin: '2rem auto' }}>
        <h2>Login</h2>
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

          <button type="submit" className="login-btn">Login</button>

        </form>
        <p style={{ marginTop: '1rem', textAlign: 'center' }}>
          Don't have an account? <Link to="/register">Register</Link>
        </p>
      </section>
    </main>
  )
}

export default LoginPage