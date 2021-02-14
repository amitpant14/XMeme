import React, { useEffect, useState, useContext } from "react";
import { ThemeContext } from "providers/ThemeProvider";
import { Container, Card } from "components/common";
import axios from "axios";
import { Wrapper, Grid, Item, Content } from "./styles";
import notFound from "assets/images/memeNotFound.png";

export const Display = () => {
  const { theme } = useContext(ThemeContext);
  const [memes, setMemes] = useState([]);
  useEffect(() => {
    axios
      .get(`${process.env.BACKEND_URL}`)
      .then((response) => response.data)
      .then((memeData) => {
        memeData.sort((a, b) =>
          a.id < b.id ? 1 : -1
        );
        setMemes(memeData);
      })
      .catch((error) => console.log(error));
  }, []);
  return (
    <Wrapper as={Container} id="projects">
      {memes.length > 0}
      <Grid>
        {memes.map((node) => (
          <Item theme={theme}>
            <Card theme={theme}>
              <Content>
                <h4>{node.name}</h4>
                <p>{node.caption}</p>
                <img src={node.url} onError={(e)=>{ if (e.target.src !== notFound)
                  {e.target.onerror = null; e.target.src=notFound}}}/>
              </Content>
            </Card>
          </Item>
        ))}
      </Grid>
    </Wrapper>
  );
};
