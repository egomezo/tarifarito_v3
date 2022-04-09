<template>
  <div class="sidebar-logo-container" :class="{'collapse':collapse}">
    <transition name="sidebarLogoFade">
      <a v-if="collapse" key="collapse" class="sidebar-logo-link" href="#">
        <img v-if="logo" :src="logo" class="sidebar-logo">
        <h1 v-else class="sidebar-title">{{ title }} </h1>
      </a>
      <a v-else key="expand" router-link class="sidebar-logo-link" href="#">
        <img v-if="logo" :src="logo" class="sidebar-logo">
        <h1 class="sidebar-title">{{ title }} </h1>
      </a>
    </transition>
  </div>
</template>

<script>
import logPage from '../../../assets/superservicios1.png'
import { mapGetters } from 'vuex'
import { getDependencia } from '@/api/procesosDIEG/dependencia'

export default {
  name: 'SidebarLogo',
  props: {
    collapse: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      title: 'Procesos',
      logo: logPage,
      datosDependencia: []
    }
  },
  computed: {
    ...mapGetters(['dependencia'])
  },
  created() {
    this.getInfoDependencia()
  },
  methods: {
    async getInfoDependencia() {
      await getDependencia(this.dependencia).then((response) => {
        this.datosDependencia = response[0]
        this.title = this.title + ' ' + this.datosDependencia.descripcion
        // console.log('Dependencia -> ', this.title)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.sidebarLogoFade-enter-active {
  transition: opacity 1.5s;
}

.sidebarLogoFade-enter,
.sidebarLogoFade-leave-to {
  opacity: 0;
}

.sidebar-logo-container {
  position: relative;
  width: 100%;
  height: 50px;
  line-height: 50px;
  background: #2b2f3a;
  text-align: center;
  overflow: hidden;

  & .sidebar-logo-link {
    height: 100%;
    width: 100%;

    & .sidebar-logo {
      width: 32px;
      height: 32px;
      vertical-align: middle;
      margin-right: 12px;
    }

    & .sidebar-title {
      display: inline-block;
      margin: 0;
      color: #fff;
      font-weight: 600;
      line-height: 50px;
      font-size: 14px;
      font-family: Avenir, Helvetica Neue, Arial, Helvetica, sans-serif;
      vertical-align: middle;
    }
  }

  &.collapse {
    .sidebar-logo {
      margin-right: 0px;
    }
  }
}
</style>
