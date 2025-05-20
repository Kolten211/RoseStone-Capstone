import { useEffect, useState } from "react";
import {  Outlet } from "react-router-dom";
import { useDispatch } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";
import FooterNavigation from "../components/Footer/Footer";

export default function Layout() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  // const sessionUser = useSelector(state => state.session.user);


  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  if (!isLoaded) {
    return <div>Loading...</div>
  }

  // if (!sessionUser) {
  //   return <Navigate to='login'  replace />
  // }

  return (
    <>
      <ModalProvider>
        <Navigation />
        {isLoaded && <Outlet />}
        <Modal />
        <FooterNavigation />
      </ModalProvider>
    </>
  );
}
