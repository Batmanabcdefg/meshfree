! shape function{{{
subroutine shape(numSmpl,x,numNode,xi,dm,nip,ipnode,phi)
    implicit none
    integer, intent(in) :: numNode, numSmpl
    real(kind = 8), intent(in) :: x(3,numSmpl), xi(3,numNode)
    real(kind = 8), intent(in) :: dm(3,numNode)
    integer, intent(out) :: nip(numSmpl+1), ipnode(1)
    real(kind = 8), intent(out) :: phi(1)

    ! local variables
    integer :: i

    do i = 1,numSmpl
        call finode(x(1,i),numNode,x,dm,nip(i+1),ipnode(nip(i)))
    enddo
    
    
end subroutine shape
!}}}
! find nodes{{{
subroutine finode(gpos,numNode,x,dm,nip,ipnode)
    implicit none
    integer, intent(in) :: numNode
    real(kind = 8), intent(in) :: gpos(3), x(3,numNode)
    real(kind = 8), intent(in) :: dm(3,numNode)
    integer, intent(out) :: nip, ipnode(1)

    ! local variables
    integer :: i, ind = 0
    real(kind = 8) :: rx, ry, rz

    print*, gpos
    print*, x(1,1)
    print*, numNode
    print*, dm(1,1)
    
    do i = 1,numNode
        rx = abs(x(1,i) - gpos(1))/dm(1,i)
        ry = abs(x(2,i) - gpos(2))/dm(2,i)
        rz = abs(x(3,i) - gpos(3))/dm(3,i)
        ! check close
        if(rx < 1.D0 .and. ry < 1.D0 .and.rz < 1.D0)then
            ind = ind + 1
            ipnode(ind) = i
        endif
    enddo
    nip = ind
    return
end subroutine finode
!}}}

subroutine foo(a,n)
    implicit none
!    real(kind = 8), intent(in) :: a(3,1)
    integer :: n
    integer :: a(3,n)
    !f2py integer, intent(in) :: a(3,n)
    !f2py integer, intent(hide), depend(a) :: n = shape(a,1)
    integer :: i
    print*, 'Hello world!\n'
    print*, 'a = %i', (a(i,n),i = 1,3)
end subroutine foo
