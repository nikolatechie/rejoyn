import { useState } from "react";

export default function Register() {
  const [fullName, setFullName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [dob, setDob] = useState('')
  const [gender, setGender] = useState('Male')

  const onRegister = async (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();

    try {
      const response = await fetch(
        `http://0.0.0.0:8000/register`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            full_name: fullName,
            email,
            password,
            dob,
            gender
          })
        }
      );
      // const data = await response.json();
      if (response.ok) {
        // success
        console.log("success");
        // console.log(data);
      } else {
        console.log("fail");
        // alert(data.errorMessage);
      }
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <div style={{
      maxWidth: "50%",
      margin: "auto",
      marginTop: "100px"
    }}>
      <div className="mb-3">
        <label htmlFor="fullName" className="form-label">Full name</label>
        <input
          type="text"
          className="form-control"
          id="fullName"
          onChange={(e) => setFullName(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="email" className="form-label">Email address</label>
        <input
          type="email"
          className="form-control"
          id="email"
          placeholder="name@example.com"
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="password" className="form-label">Password</label>
        <input
          type="password"
          className="form-control"
          id="password"
          placeholder=""
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="dob" className="form-label">Date of birth</label>
        <input
          type="date"
          className="form-control"
          id="dob"
          placeholder=""
          onChange={(e) => setDob(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="gender" className="form-label">Gender</label>
        <select
          className="form-control"
          id="gender"
          onChange={(e) => setGender(e.target.value)}
        >
          <option value="Male">Male</option>
          <option value="Female">Female</option>
          <option value="Other">Other</option>
        </select>
      </div>
      <div className="mb-3" style={{ textAlign: "right" }}>
        <button type="button" className="btn btn-primary" onClick={onRegister}>Register</button>
      </div>
    </div>
  )
}
