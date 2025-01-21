import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import PrivateRoute from '../components/PrivateRouteComponent/PrivateRoute';
import LandingPage from '../components/LandingPage';
import Greeting from '../components/Greeting/GreetingPage';




export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <PrivateRoute>
                  <Greeting />
                </PrivateRoute>
      },
      {
        path: '/landing-page',
        element: <LandingPage />
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
    ],
  },
]);