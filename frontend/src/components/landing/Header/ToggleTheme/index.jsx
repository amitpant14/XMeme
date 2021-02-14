import React, { useContext } from 'react';
import { ThemeContext } from 'providers/ThemeProvider';
import sunIcon from 'assets/images/sun.svg';
import moonIcon from 'assets/images/moon.svg';
import { Wrapper } from './styles';

const ToggleTheme = () => {
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <Wrapper type="button" onClick={toggleTheme}>
      <img src={theme === 'light' ? moonIcon : sunIcon} alt={theme} />
    </Wrapper>
  );
};

export default ToggleTheme;
