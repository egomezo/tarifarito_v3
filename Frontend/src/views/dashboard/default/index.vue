<template>
  <div class="div-cont">
    <el-row class="cont-row">
      <el-col :span="24">
        <aside>
          <span class="text-header">
            <b>DIRECCIÓN TÉCNICA DE GESTIÓN DE ENERGÍA</b>
          </span>
        </aside>
      </el-col>
      <el-col :span="24">
        <aside>
          <span class="text-user">
            <b>{{ name }}</b>
          </span>
        </aside>
      </el-col>
    </el-row>
    <el-row class="cont-logo">
      <el-col :sm="24" :md="10" class="div-cont-logo">
        <img :src="logo" class="imagePng">
      </el-col>
      <el-col :sm="24" :md="14" class="div-text-logo">
        <el-row>
          <el-col :span="24">
            <span class="text-superservicios">
              <b>Superservicios</b>
            </span>
          </el-col>
          <el-col :span="24">
            <span class="text-nombre">Superintendencia de Servicios</span>
          </el-col>
          <el-col :span="24">
            <span class="text-nombre">Públicos Domiciliarios</span>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import logSuper from '@/assets/superservicios1.png'

export default {
  name: 'DashboardDefault',
  components: {},
  data() {
    return {
      logo: logSuper
    }
  },
  computed: {
    ...mapGetters(['name', 'avatar', 'roles'])
  }
}
</script>

<style lang="scss" scoped>
	.div-cont {
		padding: 1em;
	}

	.text-header {
		color: black;
	}

	.imagePng {
		width: 21vh;
	}

	.cont-logo {
		border: 0px solid;
		height: 22vh;
    margin: 1em;
	}

  .div-cont-logo {
    border: 0px solid red;
    height: 100%;
  }

  .div-text-logo {
    border: 0px solid blue;
    height: 100%;
  }

	.cont-row {
		text-align: center;
	}

	// Pantallas superiores a 800px (PC)
	@media screen and (min-width: 800px) {
		.text-header {
			font-size: x-large;
		}

		.text-user {
			font-size: large;
		}

    .div-cont-logo {
      text-align: right;
    }

    .div-text-logo {
      display: flex;
      align-items: center;
    }

    .text-superservicios {
      font-size: xx-large;
    }

    .text-nombre {
      font-size: medium;
    }
	}

	// Pantallas inferiores a 800px (mobile)
	@media screen and (max-width: 800px) {
		.text-header {
			font-size: small;
		}

		.text-user {
			font-size: small;
		}

    .div-cont-logo {
      text-align: center;
    }

    .div-text-logo {
      text-align: center;
    }

    .text-superservicios {
      font-size: xx-large;
    }

    .text-nombre {
      font-size: medium;
    }
	}
</style>
