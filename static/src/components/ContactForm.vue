<template>
  <v-row
    id="wrapper"
    align="center"
    justify="center"
  >
    <v-col
      lg="4"
      md="7"
      sm="7"
    >
      <v-card width="100%">
        <v-card-title>Contact Us</v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              v-model="form.name"
              label="Name"
              :disabled="disabled"
              clearable
            />
            <v-text-field
              v-model="form.email"
              type="email"
              :disabled="disabled"
              label="Email Address"
              clearable
            />
            <v-text-field
              v-model="form.subject"
              label="Subject"
              :disabled="disabled"
              clearable
            />
            <v-textarea
              v-model="form.message"
              :disabled="disabled"
              label="Message"
            />

            <v-btn
              type="submit"
              block
              :disabled="disabled"
              color="accent"
              @click.prevent="submit"
            >
              Send
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ContactForm',

  data: () => ({
    form: {
      name: null,
      email: null,
      subject: null,
      message: null
    },
    disabled: false
  }),

  methods: {
    submit () {
      this.disabled = true
      console.log(this.name)
      axios.post('/contact', this.form).then(res => {
        console.log(res)
        this.form.name = null
        this.form.email = null
        this.form.subject = null
        this.form.message = null
        alert('Thank you for your message!')
      }).catch(err => {
        console.error(err)
        alert('Sorry, we could not complete your request.')
      }).finally(() => {
        this.disabled = false
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  #wrapper {
    height: 100%;
  }
</style>
