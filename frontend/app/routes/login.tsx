import { useState } from "react";
import { useNavigate } from "react-router";

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();

    try {
      const response = await fetch(`http://0.0.0.0:8000/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email,
          password,
        }),
      });
      if (response.ok) {
        // success
        console.log("success");
        navigate("/tripform");
        // console.log(data);
      } else {
        const data = await response.json();
        console.log("fail");
        alert(data.detail);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div
      style={{
        maxWidth: "50%",
        margin: "auto",
        marginTop: "100px",
      }}
    >
      <h1 className="mb-4">Login</h1>
      <div className="mb-3">
        <label htmlFor="email" className="form-label">
          Email address
        </label>
        <input
          type="email"
          className="form-control"
          id="email"
          placeholder="name@example.com"
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="password" className="form-label">
          Password
        </label>
        <input
          type="password"
          className="form-control"
          id="password"
          placeholder=""
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <div className="mb-3" style={{ textAlign: "right" }}>
        <button type="button" className="btn btn-primary" onClick={onLogin}>
          Login
        </button>
      </div>
    </div>
  );
}
