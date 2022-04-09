<template>
  <div style="border: 0px solid blue;">
    <div style="padding-bottom: 65px">
      <sticky class-name="sub-navbar" style="position: fixed; width: 100%;">
        <div style="text-align: center; color: white">
          <el-row>
            <el-col :span="13" :xs="9" class="div-header">
              <label v-if="x.matches" style="font-size: small">{{ expediente }}</label>
              <label v-else style="font-size: x-large">Etapas expediente {{ expediente }}</label>
            </el-col>
            <el-col :span="11" :xs="15" style="border: 0px solid red; text-align: right;">
              <!-- Boton para agregar nueva etapa al aplicativo -->
              <el-button
                :disabled="!editar"
                style="border: 2px solid #67c23a"
                size="medium"
                icon="el-icon-circle-plus"
                @click="clickAgregarEtapa();"
              >Agregar etapa</el-button>
              <el-button
                style="border: 1px solid #67c23a"
                type="warning"
                size="medium"
                @click="closeModalEtapa()"
              >{{ btnClose() }}</el-button>
            </el-col>
          </el-row>
        </div>
      </sticky>
    </div>

    <!-- Cuadro de dialogo para agregar etapa -->
    <ModalAgregar
      :modaltitulo="tituloModalItem"
      :modalvisible="dialogVisibleItem"
      :modalform="formItem"
      :domcomponents="domItem"
      :rulesform="rulesFormItem"
      :datamodal="dataFormItem"
      :action="modalAction"
      @confirmar="handleConfirmar"
    />

    <!-- Listado de etapas -->
    <ListaEtapas :idproceso="idproceso" :editar="editar" :recargarlista="recargarlista" />

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Sticky from '@/components/Sticky' // 粘性header组件
import elDragDialog from '@/directive/el-drag-dialog' // base on element-ui
import { CONSTANTS } from './constants/constants'
import ListaEtapas from './ListaEtapas'
import ModalAgregar from '@/components/ModalAgregar'
import { getListEtapas, getEtapaProceso, createEtapa } from '@/api/procesosDIEG/etapas'

export default {
  name: 'Etapas',
  components: { Sticky, ListaEtapas, ModalAgregar },
  directives: { elDragDialog },
  props: {
    editar: {
      type: Boolean,
      default: false
    },
    idproceso: {
      type: String,
      default: ''
    },
    expediente: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      formItem: CONSTANTS.formItem,
      domItem: CONSTANTS.domItem,
      rulesFormItem: CONSTANTS.rulesFormItem,
      dataFormItem: CONSTANTS.dataFormItem,
      /* Si es o no visible el cuadro de dialogo de agregar o editar etapa */
      dialogVisibleItem: false,
      tituloModalItem: '',
      modalAction: '',
      x: '',
      recargarlista: false,
      datosEtapaProceso: []
    }
  },
  computed: {
    ...mapGetters(['name', 'roles', 'idusuario', 'dependencia'])
  },
  async mounted() {
    this.formItem = {} // Permite inicializar el modelo que utiliza el modal de agregar
    this.x = window.matchMedia('(max-width: 800px)')
  },
  created() {
    this.initView()
  },
  methods: {
    async initView() {
      this.cargarEtapas()
    },
    btnClose() {
      if (this.x.matches) {
        return 'X'
      } else {
        return 'Cerrar'
      }
    },
    cargarEtapas() {
      this.getEtapasProceso()
      this.getEtapas()
    },
    async getEtapasProceso() {
      await getEtapaProceso(this.idproceso).then((response) => {
        // console.log('ETAPAs DEL PROCESO -> ', response)
        this.datosEtapaProceso = response
      })
    },
    async getEtapas() {
      await getListEtapas().then((response) => {
        // console.log('Etapas --> ', response)
        const datosEtapa = response
        for (const iterator of this.datosEtapaProceso) {
          datosEtapa.filter((etapa) => {
            if (etapa.id === iterator.etapa) { // Verifica si la etapa ya esta en el proceso
              if (iterator.varios_actos === 'NO') { // Verifica que no tenga varios actos y se elimina del arreglo de etapas que se muestra en el select de etapas
                const posEtapa = datosEtapa.indexOf(etapa) // Obtiene la posicion de la etapa en el arreglo
                datosEtapa.splice(posEtapa, 1) // Elimina la posicion de la etapa del arreglo
              }
            }
          })
        }
        this.dataFormItem.etapa = datosEtapa
      })
    },
    closeModalEtapa() {
      this.$emit('close-modal-etapas')
    },
    clickAgregarEtapa() {
      this.domItem[0]['disabled'] = false // Se modifican las opciones del select
      this.rulesFormItem['etapa'][0]['required'] = true // Se modifican las reglas del select
      this.tituloModalItem = 'Agregar etapa'
      this.modalAction = 'Agregar'
      this.dialogVisibleItem = true
      this.cargarEtapas()
    },
    async handleConfirmar(modal) { // Funcion que captura los eventos que devuelve el modal de agregar etapa
      // console.log(modal)
      if (modal.response) {
        // Se realiza la acción de crear etapa
        modal.data.idproceso = parseInt(this.idproceso)
        await this.getNumeroacto(this.idproceso, modal.data.etapa).then((res) => { modal.data.numeroacto = res })
        await createEtapa(modal.data).then(async(response) => {
          // console.log('RESPONSE AGREGAR -> ', response)
          this.$notify({
            title: 'Buen trabajo parcero!',
            message: 'Etapa agregada con éxito',
            type: 'success',
            duration: 2000
          })
          this.recargarlista = true // Permite actualizar la vista de la lista de etapas (importante)
        })
      }
      this.dialogVisibleItem = false
      this.formItem = {} // Se reinicia el modelo del modal (importante)
      this.dataFormItem.etapa = [] // Permite reiniciar el arreglo de etapas del modal (Debido a que los datos quedan cacheados)
      this.recargarlista = false // Permite actualizar la vista de la lista de etapas, reinicia la variable (observable de lista etapas)
    },
    async getNumeroacto(idproceso, idetapa) {
      let numeroacto = 0
      await getEtapaProceso(idproceso, idetapa).then((response) => {
        // console.log('ETAPA_PROCESO -> ', response)
        if (response.length) {
          // console.log('tiene actos')
          numeroacto = response.length + 1
        } else {
          // console.log('No tiene actos')
          numeroacto = 1
        }
      })
      // console.log('numeroacto --> ', numeroacto)
      return numeroacto
    }
  }
}
</script>

<style lang="scss">
  // Pantallas superiores a 800px (PC)
  @media screen and (min-width: 800px) {
    .div-header {
      text-align: right;
    }
  }

  // Pantallas inferiores a 800px (mobile)
  @media screen and (max-width: 800px) {
    .div-header {
      text-align: center;
    }
  }
</style>
