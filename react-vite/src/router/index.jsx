import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import PrivateRoute from '../components/PrivateRouteComponent/PrivateRoute';
import LandingPage from '../components/LandingPage';
import Greeting from '../components/Greeting/GreetingPage';
import LessonDetails from '../components/LessonDetails/LessonDetails';
import WordBox from '../components/UsersWordsPhrases/UserContent';
import CreateWord from '../components/CreateWord/CreateWord';
import ProfilePage from '../components/ProfilePage/ProfilePage';
import UpdateWord from '../components/UpdateWord/UpdateWord';
import PhraseBuilder from '../PhraseBuilder/PhraseBuilder';
import WordDetails from '../components/WordDetails/WordDetails';
import LearnedPhrases from '../components/PhraseContent/Phrases';
// import VoiceRecorder from '../components/UpdateWord/Recorder';




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
        path:'/learned-phrases',
        element: <LearnedPhrases />
      },
      { 
        path: '/learned-words',
        element: <WordBox />

      },
      {
        path: '/learned/:word_id',
        element: <UpdateWord />
      },
      {
        path:'/learned/:word_id/details',
        element: <WordDetails />
      },
      {
        path: '/phrase-builder',
        element: <PhraseBuilder />
      },
      // {
      //   path: '/audio-record',
      //   element: <VoiceRecorder />
      // },
      {
        path: '/create-word',
        element: <CreateWord />
      },
      {
        path: '/lesson/:lesson_id',
        element: <LessonDetails />
      },
      {
        path: '/profile-page',
        element: <ProfilePage />
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