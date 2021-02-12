import React, { useContext, useEffect, useState } from 'react';
import { ThemeContext } from 'providers/ThemeProvider';
import { GatsbySeo } from 'gatsby-plugin-next-seo';
import { Global } from './styles';

import './fonts.css';

export const Layout = ({ children }) => {
  const { theme } = useContext(ThemeContext);
  const [url, setUrl] = useState('');
  useEffect(() => {
    setUrl(window.location.href);
  }, []);
  return (
    <>
      <GatsbySeo
        title={"XMeme"}
        description="A Meme sharing full-stack application"
        canonical={url}
        openGraph={{
          type: 'website',
          title: "XMeme",
          site_name: "XMeme",
          locale: 'en_IN',
          url,
          description: "Share all the funny memes you have.",
        }}
      />
      <Global theme={ theme } />
      {children}
      {/* <Footer /> */}
    </>
  );
};
