import React from 'react';
import axios from 'axios';
import { Formik, Form, FastField, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { Button, Input } from 'components/common';
import { Error, Center, InputField, Wrapper } from './styles';

export default () => (
  <Wrapper>
    <h2>Submit your meme</h2>
    <Formik
      initialValues={{
        name: '',
        caption: '',
        url: '',
        success: false,
      }}
      validationSchema={Yup.object().shape({
        name: Yup.string().trim().required('Full name is mandatory'),
        caption: Yup.string().trim().required('Caption is mandatory'),
        url: Yup.string().trim().url('Please enter a valid url').required('URL is mandatory'),
      })}
      onSubmit={async ({ name, caption, url }, { setSubmitting, resetForm, setFieldValue }) => {
        try {
          await axios({
            method: 'POST',
            url: `${process.env.BACKEND_URL}`,
            headers: {
              'Content-Type': 'application/json',
            },
            data: JSON.stringify({
              name,
              caption,
              url,
            }),
          });
          setSubmitting(false);
          setFieldValue('success', true);
          setTimeout(() => resetForm(), 3000);
        } catch (err) {
          setSubmitting(false);
          setFieldValue('success', false);
          alert("Something went wrong, please try again!"); // eslint-disable-line
        }
      }}
    >
      {({ values, touched, errors, setFieldValue, isSubmitting }) => (
        <Form>
          <InputField>
            <Input
              as={FastField}
              type="text"
              name="name"
              component="input"
              aria-label="name"
              placeholder="Your name*"
              error={touched.name && errors.name}
            />
            <ErrorMessage component={Error} name="name" />
          </InputField>
          <InputField>
            <Input
              as={FastField}
              component="textarea"
              aria-label="caption"
              id="caption"
              rows="8"
              type="text"
              name="caption"
              placeholder="Caption*"
              error={touched.message && errors.message}
            />
            <ErrorMessage component={Error} name="caption" />
          </InputField>
          <InputField>
            <Input
              as={FastField}
              type="text"
              name="url"
              component="input"
              aria-label="url"
              placeholder="URL*"
              error={touched.name && errors.name}
            />
            <ErrorMessage component={Error} name="url" />
          </InputField>
          {values.success && (
            <InputField>
              <Center>
                <h4>Your meme has been updated in the database successfully! Please reload the page to check it out.</h4>
               </Center>
             </InputField>
          )
          }
          <Center>
            <Button secondary type="submit" disabled={isSubmitting} className="submit-btn">
              Submit
            </Button>
          </Center>
        </Form>
      )}
    </Formik>
  </Wrapper>
);
