import { useState } from "react";
import * as sessionActions from "../../redux/session";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";
import { useModal } from "../../context/Modal";
import { thunkLogin } from "../../redux/session";
import "./LoginForm.css";

function LoginFormPage() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const { closeModal } = useModal();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});

  if (sessionUser) return <Navigate to="/" replace={true} />;

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      navigate("/");
    }
  };
  const demoUser = () => {
    return dispatch(sessionActions.thunkLogin({email:'demo@aa.io', password:'password'}))
    .then(closeModal)
    .catch(async (res) => {
      const data= await res.json();
      if (data && data.errors) {
        setErrors(data.errors);
      }
    })
  }

  return (
    <>
      <h1>Iniciar sesión</h1>
      {errors.length > 0 &&
        errors.map((message) => <p key={message}>{message}</p>)}
      <form onSubmit={handleSubmit}>
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p>{errors.email}</p>}
        <label>
          Contraseña
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p>{errors.password}</p>}
        <button type="submit">Entrar</button>
        <button onClick={demoUser}>Demo User</button>
      </form>
    </>
  );
}

export default LoginFormPage;
