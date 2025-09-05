class Usuario {
  final int id;
  final String username;
  final String email;
  final String firstName;
  final String lastName;
  final DateTime dateJoined;

  Usuario({
    required this.id,
    required this.username,
    required this.email,
    required this.firstName,
    required this.lastName,
    required this.dateJoined,
  });

  factory Usuario.fromJson(Map<String, dynamic> json) {
    return Usuario(
      id: json['id'],
      username: json['username'],
      email: json['email'],
      firstName: json['first_name'] ?? '',
      lastName: json['last_name'] ?? '',
      dateJoined: DateTime.parse(json['date_joined']),
    );
  }

  String get fullName => '$firstName $lastName'.trim();
}

class PerfilUsuario {
  final String id;
  final Usuario user;
  final String ci;
  final String telefono;
  final String telefonoEmergencia;
  final DateTime? fechaNacimiento;
  final String? fotoPerfil;
  final bool activo;
  final DateTime fechaRegistro;
  final DateTime? ultimoAcceso;

  PerfilUsuario({
    required this.id,
    required this.user,
    required this.ci,
    required this.telefono,
    required this.telefonoEmergencia,
    this.fechaNacimiento,
    this.fotoPerfil,
    required this.activo,
    required this.fechaRegistro,
    this.ultimoAcceso,
  });

  factory PerfilUsuario.fromJson(Map<String, dynamic> json) {
    return PerfilUsuario(
      id: json['id'],
      user: Usuario.fromJson(json['user']),
      ci: json['ci'] ?? '',
      telefono: json['telefono'] ?? '',
      telefonoEmergencia: json['telefono_emergencia'] ?? '',
      fechaNacimiento: json['fecha_nacimiento'] != null 
          ? DateTime.parse(json['fecha_nacimiento'])
          : null,
      fotoPerfil: json['foto_perfil'],
      activo: json['activo'] ?? true,
      fechaRegistro: DateTime.parse(json['fecha_registro']),
      ultimoAcceso: json['ultimo_acceso'] != null 
          ? DateTime.parse(json['ultimo_acceso'])
          : null,
    );
  }
}

class Condominio {
  final String id;
  final String nombre;
  final String direccion;
  final String? telefono;
  final String? email;
  final String nit;
  final String ciudad;
  final String pais;
  final bool activo;

  Condominio({
    required this.id,
    required this.nombre,
    required this.direccion,
    this.telefono,
    this.email,
    required this.nit,
    required this.ciudad,
    required this.pais,
    required this.activo,
  });

  factory Condominio.fromJson(Map<String, dynamic> json) {
    return Condominio(
      id: json['id'],
      nombre: json['nombre'],
      direccion: json['direccion'],
      telefono: json['telefono'],
      email: json['email'],
      nit: json['nit'],
      ciudad: json['ciudad'] ?? 'Santa Cruz',
      pais: json['pais'] ?? 'Bolivia',
      activo: json['activo'] ?? true,
    );
  }
}

class Unidad {
  final String id;
  final String numero;
  final int piso;
  final String? bloque;
  final double? metrosCuadrados;
  final int dormitorios;
  final int baños;
  final double porcentajePropiedad;
  final bool activa;

  Unidad({
    required this.id,
    required this.numero,
    required this.piso,
    this.bloque,
    this.metrosCuadrados,
    required this.dormitorios,
    required this.baños,
    required this.porcentajePropiedad,
    required this.activa,
  });

  factory Unidad.fromJson(Map<String, dynamic> json) {
    return Unidad(
      id: json['id'],
      numero: json['numero'],
      piso: json['piso'],
      bloque: json['bloque'],
      metrosCuadrados: json['metros_cuadrados']?.toDouble(),
      dormitorios: json['dormitorios'] ?? 1,
      baños: json['baños'] ?? 1,
      porcentajePropiedad: (json['porcentaje_propiedad'] ?? 0).toDouble(),
      activa: json['activa'] ?? true,
    );
  }

  String get identificador {
    return bloque != null ? '$bloque-$numero' : numero;
  }
}

class CuotaMantenimiento {
  final String id;
  final double montoAdministracion;
  final double montoMantenimiento;
  final double montoSeguridad;
  final double montoLimpieza;
  final double montoGastosExtras;
  final double montoMultas;
  final double montoMora;
  final double montoTotal;
  final double montoPagado;
  final double montoPendiente;
  final String estado;
  final DateTime fechaVencimiento;
  final DateTime fechaGeneracion;
  final DateTime? fechaUltimoPago;

  CuotaMantenimiento({
    required this.id,
    required this.montoAdministracion,
    required this.montoMantenimiento,
    required this.montoSeguridad,
    required this.montoLimpieza,
    required this.montoGastosExtras,
    required this.montoMultas,
    required this.montoMora,
    required this.montoTotal,
    required this.montoPagado,
    required this.montoPendiente,
    required this.estado,
    required this.fechaVencimiento,
    required this.fechaGeneracion,
    this.fechaUltimoPago,
  });

  factory CuotaMantenimiento.fromJson(Map<String, dynamic> json) {
    return CuotaMantenimiento(
      id: json['id'],
      montoAdministracion: (json['monto_administracion'] ?? 0).toDouble(),
      montoMantenimiento: (json['monto_mantenimiento'] ?? 0).toDouble(),
      montoSeguridad: (json['monto_seguridad'] ?? 0).toDouble(),
      montoLimpieza: (json['monto_limpieza'] ?? 0).toDouble(),
      montoGastosExtras: (json['monto_gastos_extras'] ?? 0).toDouble(),
      montoMultas: (json['monto_multas'] ?? 0).toDouble(),
      montoMora: (json['monto_mora'] ?? 0).toDouble(),
      montoTotal: (json['monto_total'] ?? 0).toDouble(),
      montoPagado: (json['monto_pagado'] ?? 0).toDouble(),
      montoPendiente: (json['monto_pendiente'] ?? 0).toDouble(),
      estado: json['estado'] ?? 'PENDIENTE',
      fechaVencimiento: DateTime.parse(json['fecha_vencimiento']),
      fechaGeneracion: DateTime.parse(json['fecha_generacion']),
      fechaUltimoPago: json['fecha_ultimo_pago'] != null 
          ? DateTime.parse(json['fecha_ultimo_pago'])
          : null,
    );
  }

  bool get isPendiente => estado == 'PENDIENTE';
  bool get isPagada => estado == 'PAGADA';
  bool get isVencida => estado == 'VENCIDA';
  bool get isPagadaParcial => estado == 'PAGADA_PARCIAL';
}

class AreaComun {
  final String id;
  final String nombre;
  final String descripcion;
  final int capacidadMaxima;
  final double precioPorHora;
  final bool requiereDeposito;
  final double montoDeposito;
  final String horaApertura;
  final String horaCierre;
  final List<String> diasDisponibles;
  final String? equipamiento;
  final String? reglas;
  final String? imagen;
  final bool activa;

  AreaComun({
    required this.id,
    required this.nombre,
    required this.descripcion,
    required this.capacidadMaxima,
    required this.precioPorHora,
    required this.requiereDeposito,
    required this.montoDeposito,
    required this.horaApertura,
    required this.horaCierre,
    required this.diasDisponibles,
    this.equipamiento,
    this.reglas,
    this.imagen,
    required this.activa,
  });

  factory AreaComun.fromJson(Map<String, dynamic> json) {
    return AreaComun(
      id: json['id'],
      nombre: json['nombre'],
      descripcion: json['descripcion'] ?? '',
      capacidadMaxima: json['capacidad_maxima'] ?? 0,
      precioPorHora: (json['precio_por_hora'] ?? 0).toDouble(),
      requiereDeposito: json['requiere_deposito'] ?? false,
      montoDeposito: (json['monto_deposito'] ?? 0).toDouble(),
      horaApertura: json['hora_apertura'] ?? '08:00',
      horaCierre: json['hora_cierre'] ?? '22:00',
      diasDisponibles: List<String>.from(json['dias_disponibles'] ?? []),
      equipamiento: json['equipamiento'],
      reglas: json['reglas'],
      imagen: json['imagen'],
      activa: json['activa'] ?? true,
    );
  }
}

class ReservaAreaComun {
  final String id;
  final AreaComun areaComun;
  final DateTime fechaReserva;
  final String horaInicio;
  final String horaFin;
  final int numeroPersonas;
  final String proposito;
  final String observaciones;
  final String estado;
  final double montoTotal;
  final bool depositoPagado;
  final DateTime fechaCreacion;

  ReservaAreaComun({
    required this.id,
    required this.areaComun,
    required this.fechaReserva,
    required this.horaInicio,
    required this.horaFin,
    required this.numeroPersonas,
    required this.proposito,
    required this.observaciones,
    required this.estado,
    required this.montoTotal,
    required this.depositoPagado,
    required this.fechaCreacion,
  });

  factory ReservaAreaComun.fromJson(Map<String, dynamic> json) {
    return ReservaAreaComun(
      id: json['id'],
      areaComun: AreaComun.fromJson(json['area_comun']),
      fechaReserva: DateTime.parse(json['fecha_reserva']),
      horaInicio: json['hora_inicio'],
      horaFin: json['hora_fin'],
      numeroPersonas: json['numero_personas'] ?? 1,
      proposito: json['proposito'] ?? '',
      observaciones: json['observaciones'] ?? '',
      estado: json['estado'] ?? 'PENDIENTE',
      montoTotal: (json['monto_total'] ?? 0).toDouble(),
      depositoPagado: json['deposito_pagado'] ?? false,
      fechaCreacion: DateTime.parse(json['fecha_creacion']),
    );
  }

  bool get isPendiente => estado == 'PENDIENTE';
  bool get isConfirmada => estado == 'CONFIRMADA';
  bool get isCancelada => estado == 'CANCELADA';
  bool get isCompletada => estado == 'COMPLETADA';
}

class MetodoPago {
  final String id;
  final String nombre;
  final String descripcion;
  final bool requiereComprobante;
  final bool activo;
  final bool esOnline;

  MetodoPago({
    required this.id,
    required this.nombre,
    required this.descripcion,
    required this.requiereComprobante,
    required this.activo,
    required this.esOnline,
  });

  factory MetodoPago.fromJson(Map<String, dynamic> json) {
    return MetodoPago(
      id: json['id'],
      nombre: json['nombre'],
      descripcion: json['descripcion'] ?? '',
      requiereComprobante: json['requiere_comprobante'] ?? true,
      activo: json['activo'] ?? true,
      esOnline: json['es_online'] ?? false,
    );
  }
}

class Pago {
  final String id;
  final CuotaMantenimiento cuota;
  final MetodoPago metodoPago;
  final double montoPagado;
  final String numeroTransaccion;
  final String? numeroComprobante;
  final DateTime fechaPago;
  final String estado;
  final String? observaciones;

  Pago({
    required this.id,
    required this.cuota,
    required this.metodoPago,
    required this.montoPagado,
    required this.numeroTransaccion,
    this.numeroComprobante,
    required this.fechaPago,
    required this.estado,
    this.observaciones,
  });

  factory Pago.fromJson(Map<String, dynamic> json) {
    return Pago(
      id: json['id'],
      cuota: CuotaMantenimiento.fromJson(json['cuota']),
      metodoPago: MetodoPago.fromJson(json['metodo_pago']),
      montoPagado: (json['monto_pagado'] ?? 0).toDouble(),
      numeroTransaccion: json['numero_transaccion'] ?? '',
      numeroComprobante: json['numero_comprobante'],
      fechaPago: DateTime.parse(json['fecha_pago']),
      estado: json['estado'] ?? 'PENDIENTE',
      observaciones: json['observaciones'],
    );
  }

  bool get isCompletado => estado == 'COMPLETADO';
  bool get isPendiente => estado == 'PENDIENTE';
  bool get isFallido => estado == 'FALLIDO';
}

class Notificacion {
  final String id;
  final String tipo;
  final String titulo;
  final String mensaje;
  final DateTime fecha;
  final bool leida;
  final String prioridad;
  final Map<String, dynamic>? datosAdicionales;

  Notificacion({
    required this.id,
    required this.tipo,
    required this.titulo,
    required this.mensaje,
    required this.fecha,
    required this.leida,
    required this.prioridad,
    this.datosAdicionales,
  });

  factory Notificacion.fromJson(Map<String, dynamic> json) {
    return Notificacion(
      id: json['id'],
      tipo: json['tipo'],
      titulo: json['titulo'],
      mensaje: json['mensaje'],
      fecha: DateTime.parse(json['fecha']),
      leida: json['leida'] ?? false,
      prioridad: json['prioridad'] ?? 'MEDIA',
      datosAdicionales: json['datos_adicionales'],
    );
  }

  bool get isAviso => tipo == 'AVISO';
  bool get isAlerta => tipo == 'ALERTA';
  bool get isEmergencia => tipo == 'EMERGENCIA';
  bool get isPago => tipo == 'PAGO';
  bool get isReserva => tipo == 'RESERVA';
  
  bool get isPrioridadAlta => prioridad == 'ALTA' || prioridad == 'CRITICA';
  bool get isPrioridadCritica => prioridad == 'CRITICA';
}

class QuickAction {
  final String id;
  final String titulo;
  final String descripcion;
  final String icono;
  final String color;
  final bool disponible;
  final String? url;

  QuickAction({
    required this.id,
    required this.titulo,
    required this.descripcion,
    required this.icono,
    required this.color,
    required this.disponible,
    this.url,
  });

  factory QuickAction.fromJson(Map<String, dynamic> json) {
    return QuickAction(
      id: json['id'],
      titulo: json['titulo'],
      descripcion: json['descripcion'],
      icono: json['icono'],
      color: json['color'],
      disponible: json['disponible'] ?? true,
      url: json['url'],
    );
  }
}