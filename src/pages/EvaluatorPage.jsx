import useEvaluator from '../hooks/useEvaluator'

function EvaluatorPage() {
  const {
    jobDescription, setJobDescription,
    prompt, setPrompt,
    setFile,
    status,
    errorMessage,
    result,
    handleSubmit,
  } = useEvaluator()

  return (
    <main>
      <section className="panel">
        <h2>Evaluate My Resume</h2>
        <form id="resume-form" onSubmit={handleSubmit}>

          <label htmlFor="job-description">Job Description</label>
          <textarea
            id="job-description"
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
          />

          <label htmlFor="custom-prompt">Custom Prompt</label>
          <textarea
            id="custom-prompt"
            placeholder="Enter any custom instructions..."
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />

          <label htmlFor="resume-file">Upload Resume (PDF only)</label>
          <input
            type="file"
            id="resume-file"
            accept=".pdf"
            onChange={(e) => setFile(e.target.files[0] || null)}
          />

          <button type="submit" disabled={status === 'loading'}>
            {status === 'loading' ? 'Evaluating...' : 'Evaluate Resume'}
          </button>

        </form>
      </section>

      <section className="panel">
        <h2>Results</h2>
        <div id="results">
          {status === 'idle' && <p>Results will appear here after you submit.</p>}
          {status === 'loading' && <p>Evaluating...</p>}
          {status === 'error' && <p style={{ color: 'red' }}>{errorMessage}</p>}
          {status === 'success' && <pre style={{ whiteSpace: 'pre-wrap', fontFamily: 'inherit' }}>{result}</pre>}
        </div>
      </section>
    </main>
  )
}

export default EvaluatorPage