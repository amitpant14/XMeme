import React from 'react';
import { Container } from 'components/common';
import { Wrapper, Details } from './styles';
import MemeSubmit from './MemeSubmit';

export const Forms = () => (
  <Wrapper as={Container} id="contact">
    <Details>
      <MemeSubmit />
    </Details>
  </Wrapper>
);
