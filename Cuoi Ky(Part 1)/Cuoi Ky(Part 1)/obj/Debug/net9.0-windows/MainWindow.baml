   M S B A M L   `   `   `  ����J  FCuoi Ky(Part 1), Version=1.0.0.0, Culture=neutral, PublicKeyToken=null1clr-namespace:Cuoi_Ky_Part_1_Cuoi_Ky_Part_1_  5   	        Cuoi_Ky_Part_1_.MainWindow   5   	   W SPresentationCore, Version=9.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=9.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=9.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=9.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5   	   R NSystem.Xaml, Version=9.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   /localclr-namespace:Cuoi_Ky_Part_1_     5   	   -   5          � Title$  
MainWindow��5   	   $	��450��6   $	��800��6)   .��5
      � -   5        $
��data��5
      .+�5   
   �� -   5        $	��mnv��5      $��Mã nhân viên��6   $
��Left=�62   $��	27,26,0,0q�6M   $	��Top=�6`   �� 5   
   $��Tên nhân viên��6   $
��Left=�6(   $��	27,57,0,0q�6C   $	��Top=�6V   �� 5   
   $��
Ngày sinh��6   $
��Left=�6$   $��	27,88,0,0q�6?   $	��Top=�6R   �� 5   
   $��
Phòng ban��6   $
��Left=�6$   $��
27,119,0,0q�6?   $	��Top=�6S   �� 5   
   -   5        $��txtCode��5      $
��Left=�6!   $��
137,30,0,0q�6<    �� TextWrapping$
 Wrap=�6P   $�� ��6d   $	��Top=�6l   $	��168��6�    J� RenderTransformOrigin$ 0.443,-0.521&�6�   $��22��6�   �� 5   
   -   5        $��txtFullName��5      $
��Left=�6%   $��
137,61,0,0q�6@   $
 Wrap=�6T   $�� ��6h   $	��Top=�6p   $	��168��6�   $ 0.443,-0.521&�6�   $��22��6�   (  "System.Windows.Controls.DatePicker  5   
   -   5        $��dpDOB��5      $
��Left=�6"   $��
137,90,0,0q�6=   $	��Top=�6Q   $	��168��6i   �� 5   
   -   5         ��Name$ cboDepartment��5      $
��Left=�6*   $��137,123,0,0q�6E   $	��Top=�6Z   $	��168��6r   &   System.Windows.Controls.DataGrid  5   
   -   5          Name$ danhsach��5      $��	0,173,0,0q�6%      CanUserAddRows$ False��68      AutoGenerateColumns$ False��6O      Columns 5      0  *System.Windows.Controls.DataGridTextColumn  5      ,  &System.Windows.Controls.DataGridColumn   Header$ Ma Nhan Vien��6%   	   Width5  /System.Windows.Controls.DataGridLengthConverter$	 * 6;   1  +System.Windows.Controls.DataGridBoundColumn
   Binding
 6E   �� *Code+  5      $ Ten Nhan Vien��6%   $	 * 6<   
 6F   �� *
FullName+  5      $ 	Ngay sinh��6%   $	 * 68   
 6B   �� *DateOfBirth+ �� StringFormat$ 
dd/MM/yyyy��  5      $ 	Phong ban��6%   $	 * 68   
 6B   �� *Department.Name+5      �� 5   
   -	   5        $
��Them��5      $
��Left=�6    $��
341,30,0,0q�6;   $	��Top=�6O   $��48��6g   6r   �� 5   
   -
   5        $	��Sua��5      $
��Left=�6   $��
341,63,0,0q�6:   $	��Top=�6N   $��48��6f   6q   �� 5   
   -   5        $	��Xoa��5      $
��Left=�6   $��
341,94,0,0q�6:   $	��Top=�6N   $��48��6f   6q   �� 5   
   -   5        $��Thong Ke��5      $
��Left=�6$   $��341,124,0,0q�6?   $	��Top=�6T   $��59��6l   6w   5      5       