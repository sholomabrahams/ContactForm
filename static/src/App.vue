<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-toolbar-title>
          <h1>Contact Form</h1>
        </v-toolbar-title>
      </div>
    </v-app-bar>

    <v-main>
      <ContactForm />
    </v-main>
  </v-app>
</template>

<style lang="scss" scoped>
h1 {
  font-weight: 400;
  color: #eee;
}
</style>

<script>
import ContactForm from '@/components/ContactForm'

export default {
  name: 'App',

  components: {
    ContactForm
  },

  data: () => ({
    //
  })
}
</script>
